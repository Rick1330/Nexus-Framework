name: LLM Prompt Engineering Patterns
use_when: When designing prompts for large language models, optimizing AI interactions, or implementing retrieval-augmented generation.
content: 
When implementing LLM interactions for Nexus Framework v2.6, follow these prompt engineering patterns:

1. **Task-Specific Prompting**:
   - Define clear, specific instructions for each task
   - Use imperative language for directives
   - Specify the desired output format explicitly
   - Include examples of expected inputs and outputs
   - Define constraints and limitations clearly
   - Specify evaluation criteria for the response
   - Use numbered steps for multi-step tasks

2. **Context Management**:
   - Provide relevant context at the beginning of prompts
   - Use concise but comprehensive context descriptions
   - Structure context from general to specific
   - Include only necessary information to avoid dilution
   - Use clear section headers for different context components
   - Update context dynamically based on conversation history
   - Implement context windowing for long interactions

3. **Role-Based Prompting**:
   - Define clear roles for the LLM (e.g., "You are an expert in...")
   - Specify the user's role in the interaction
   - Define the relationship between roles
   - Use role-specific terminology and expectations
   - Implement multi-role prompting for complex scenarios
   - Maintain role consistency throughout interactions
   - Use role switching when appropriate with clear transitions

4. **Few-Shot Learning**:
   - Provide 2-3 high-quality examples of desired behavior
   - Structure examples consistently with the expected task
   - Include diverse examples covering edge cases
   - Format examples identically to the expected input/output
   - Use examples of increasing complexity
   - Include explanations with examples when helpful
   - Separate examples clearly with delimiters

5. **Chain-of-Thought Prompting**:
   - Instruct the model to "think step by step"
   - Break complex reasoning into explicit steps
   - Use numbered reasoning steps for clarity
   - Demonstrate the reasoning process in examples
   - Ask for intermediate conclusions
   - Implement verification steps for critical reasoning
   - Use tree-of-thought for complex decision making

6. **Retrieval-Augmented Generation**:
   - Implement vector search for relevant knowledge retrieval
   - Use chunking strategies appropriate to content type
   - Implement re-ranking for improved relevance
   - Use clear citation formats for retrieved information
   - Implement hybrid search (vector + keyword)
   - Use metadata filtering for context relevance
   - Implement dynamic retrieval based on query analysis

7. **Output Structuring**:
   - Define explicit output formats (JSON, YAML, etc.)
   - Use examples to demonstrate the expected structure
   - Implement schema validation for structured outputs
   - Use delimiters to clearly mark output sections
   - Define fallback formats for complex outputs
   - Implement parsers for extracting structured data
   - Use consistent naming conventions in structured outputs

8. **Error Handling**:
   - Define how to handle ambiguous or incomplete inputs
   - Implement graceful degradation for edge cases
   - Specify when to ask for clarification
   - Define confidence thresholds for responses
   - Implement fallback strategies for low-confidence scenarios
   - Use structured error responses
   - Define recovery paths for common error scenarios

9. **Prompt Chaining**:
   - Break complex tasks into sub-prompts
   - Use output from one prompt as input to another
   - Implement proper context preservation between chains
   - Use intermediate validation between chain steps
   - Implement error recovery within chains
   - Use parallel prompting for independent sub-tasks
   - Implement aggregation strategies for combining results

10. **Evaluation and Refinement**:
    - Define evaluation criteria for prompt effectiveness
    - Implement automated evaluation with test cases
    - Use human evaluation for subjective quality
    - Implement A/B testing for prompt variations
    - Track performance metrics for different prompt versions
    - Use prompt versioning for systematic improvement
    - Document prompt design decisions and outcomes

Apply these patterns consistently across all LLM interactions to ensure effective, reliable, and high-quality AI capabilities.
