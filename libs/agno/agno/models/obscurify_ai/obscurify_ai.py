from dataclasses import dataclass, field
from os import getenv
from typing import Any, Dict, Optional

from agno.exceptions import ModelAuthenticationError
from agno.models.openai.like import OpenAILike


@dataclass
class ObscurifyAI(OpenAILike):
    """
    A class for interacting with Obscurify.ai, a privacy-focused, OpenAI-compatible API.

    Attributes:
        id (str): The id of the Obscurify.ai model to use. Default is "deepseek/deepseek-v4-flash".
        name (str): The name of this chat model instance. Default is "Obscurify.ai".
        provider (str): The provider of the model. Default is "Obscurify.ai".
        api_key (str): The api key to authorize request to Obscurify.ai.
        base_url (str): The base url to which the requests are sent.
            Defaults to "https://obscurify.ai/v1".
    """

    id: str = "deepseek/deepseek-v4-flash"
    name: str = "Obscurify.ai"
    provider: str = "Obscurify.ai"
    api_key: Optional[str] = field(default_factory=lambda: getenv("OBSCURIFY_API_KEY"))
    base_url: str = "https://obscurify.ai/v1"

    def _get_client_params(self) -> Dict[str, Any]:
        """
        Returns client parameters for API requests, checking for OBSCURIFY_API_KEY.

        Returns:
            Dict[str, Any]: A dictionary of client parameters for API requests.
        """
        if not self.api_key:
            self.api_key = getenv("OBSCURIFY_API_KEY")
            if not self.api_key:
                raise ModelAuthenticationError(
                    message="OBSCURIFY_API_KEY not set. Please set the OBSCURIFY_API_KEY environment variable.",
                    model_name=self.name,
                )
        return super()._get_client_params()
