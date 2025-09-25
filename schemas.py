from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for a source used by the agent"""

    name: str = Field(description="The name of the source")
    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """Schema for the response from the agent"""

    answer: str = Field(description="The answer to the question")
    sources: List[Source] = Field(
        default_factory=list, description="The sources of the answer"
    )
