"""
Nexus Framework v2.0 - Tool Registry Module

This module implements the tool registry system for the Nexus Framework,
responsible for managing and providing access to external tools and services.
"""

from typing import Dict, List, Optional, Any, Callable
import logging
import uuid

logger = logging.getLogger(__name__)

class ToolRegistry:
    """
    Central registry for external tools and services in the Nexus Framework.
    
    Provides standardized interfaces for connecting with external tools,
    managing authentication, and normalizing data formats.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Tool Registry with the provided configuration.
        
        Args:
            config: Configuration dictionary for the tool registry.
                   If None, default configuration will be used.
        """
        self.config = config or {}
        self.tools = {}
        self.adapters = {}
        self.tool_metrics = {}
        
        logger.info("Tool Registry initialized")
    
    async def register_tool(self, 
                           tool_id: str, 
                           tool_info: Dict[str, Any],
                           adapter: Optional[Callable] = None) -> bool:
        """
        Register a tool with the registry.
        
        Args:
            tool_id: Unique identifier for the tool
            tool_info: Information about the tool including capabilities
            adapter: Optional adapter function for the tool
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        if tool_id in self.tools:
            logger.warning(f"Tool {tool_id} already registered")
            return False
            
        self.tools[tool_id] = tool_info
        
        if adapter:
            self.adapters[tool_id] = adapter
        
        self.tool_metrics[tool_id] = {
            "calls": 0,
            "successes": 0,
            "failures": 0,
            "average_latency": 0
        }
        
        logger.info(f"Tool {tool_id} registered successfully")
        return True
    
    async def get_tool(self, tool_id: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a registered tool.
        
        Args:
            tool_id: Identifier of the tool to retrieve
            
        Returns:
            Optional[Dict]: Tool information or None if not found
        """
        if tool_id not in self.tools:
            logger.warning(f"Tool {tool_id} not found in registry")
            return None
            
        return self.tools[tool_id]
    
    async def execute_tool(self, 
                          tool_id: str, 
                          action: str,
                          parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an action using a registered tool.
        
        Args:
            tool_id: Identifier of the tool to use
            action: Action to perform with the tool
            parameters: Parameters for the action
            
        Returns:
            Dict: Result of the tool execution
        """
        if tool_id not in self.tools:
            logger.error(f"Cannot execute: Tool {tool_id} not found in registry")
            raise ValueError(f"Tool {tool_id} not found")
            
        # Record metrics for this call
        self.tool_metrics[tool_id]["calls"] += 1
        
        try:
            # If we have an adapter for this tool, use it
            if tool_id in self.adapters:
                adapter = self.adapters[tool_id]
                result = await adapter(action, parameters)
            else:
                # Otherwise, use a generic execution method
                result = await self._generic_tool_execution(tool_id, action, parameters)
                
            # Record success
            self.tool_metrics[tool_id]["successes"] += 1
            return result
            
        except Exception as e:
            # Record failure
            self.tool_metrics[tool_id]["failures"] += 1
            logger.error(f"Error executing tool {tool_id}: {str(e)}")
            raise
    
    async def _generic_tool_execution(self, 
                                     tool_id: str, 
                                     action: str,
                                     parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generic method for tool execution when no specific adapter is available.
        
        Args:
            tool_id: Identifier of the tool to use
            action: Action to perform with the tool
            parameters: Parameters for the action
            
        Returns:
            Dict: Result of the tool execution
        """
        # This would implement a generic execution strategy
        # For now, return a placeholder result
        logger.warning(f"Using generic execution for tool {tool_id}")
        return {
            "status": "executed",
            "tool_id": tool_id,
            "action": action,
            "execution_id": str(uuid.uuid4()),
            "result": f"Generic execution of {action} with {len(parameters)} parameters"
        }
    
    async def get_tool_metrics(self, tool_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get usage metrics for tools in the registry.
        
        Args:
            tool_id: Optional tool ID to get metrics for a specific tool
                    If None, metrics for all tools are returned
            
        Returns:
            Dict: Tool usage metrics
        """
        if tool_id:
            if tool_id not in self.tool_metrics:
                logger.warning(f"No metrics found for tool {tool_id}")
                return {}
            return {tool_id: self.tool_metrics[tool_id]}
        
        return self.tool_metrics
    
    async def list_tools(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all registered tools, optionally filtered by category.
        
        Args:
            category: Optional category to filter tools
            
        Returns:
            List[Dict]: List of tool information dictionaries
        """
        result = []
        
        for tool_id, tool_info in self.tools.items():
            if category is None or tool_info.get("category") == category:
                tool_data = {
                    "id": tool_id,
                    **tool_info,
                    "has_adapter": tool_id in self.adapters
                }
                result.append(tool_data)
                
        return result
