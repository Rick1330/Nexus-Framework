"""
Nexus Framework v2.0 - Base Agent Module

This module defines the base agent class that all specialized agents inherit from,
providing common functionality and interfaces for agent operations.
"""

from typing import Dict, List, Optional, Any
import logging
from datetime import datetime
import uuid

logger = logging.getLogger(__name__)

class BaseAgent:
    """
    Base class for all agents in the Nexus Framework.
    
    Provides common functionality and interfaces that all specialized agents
    should implement or inherit.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the base agent with the provided configuration.
        
        Args:
            config: Configuration dictionary for the agent.
                   If None, default configuration will be used.
        """
        self.agent_id = str(uuid.uuid4())
        self.config = config or {}
        self.capabilities = []
        self.status = "initialized"
        self.memory = {}
        self.created_at = datetime.now().isoformat()
        self.last_active = self.created_at
        
        logger.info(f"Agent {self.agent_id} initialized")
    
    async def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task assigned to this agent.
        
        Args:
            task: Task definition including requirements and parameters
            
        Returns:
            Dict: Result of the task processing
        """
        # This method should be overridden by specialized agents
        raise NotImplementedError("Specialized agents must implement process_task")
    
    async def update_status(self, status: str) -> None:
        """
        Update the agent's status.
        
        Args:
            status: New status for the agent
        """
        self.status = status
        self.last_active = datetime.now().isoformat()
        logger.info(f"Agent {self.agent_id} status updated to {status}")
    
    async def store_in_memory(self, key: str, value: Any) -> None:
        """
        Store information in the agent's local memory.
        
        Args:
            key: Key for storing the information
            value: Value to store
        """
        self.memory[key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
    
    async def retrieve_from_memory(self, key: str) -> Optional[Any]:
        """
        Retrieve information from the agent's local memory.
        
        Args:
            key: Key for the information to retrieve
            
        Returns:
            Optional[Any]: Retrieved value or None if not found
        """
        if key not in self.memory:
            return None
        
        return self.memory[key]["value"]
    
    async def get_capabilities(self) -> List[str]:
        """
        Get the list of capabilities this agent provides.
        
        Returns:
            List[str]: List of capability identifiers
        """
        return self.capabilities
    
    async def can_handle_task(self, task: Dict[str, Any]) -> bool:
        """
        Determine if this agent can handle the specified task.
        
        Args:
            task: Task definition to evaluate
            
        Returns:
            bool: True if the agent can handle the task, False otherwise
        """
        # Basic implementation that can be overridden by specialized agents
        required_capabilities = task.get("required_capabilities", [])
        
        if not required_capabilities:
            return True
            
        return all(cap in self.capabilities for cap in required_capabilities)
    
    async def shutdown(self) -> None:
        """
        Perform cleanup and shutdown operations for this agent.
        """
        logger.info(f"Agent {self.agent_id} shutting down")
        self.status = "shutdown"
        # Cleanup operations would go here
