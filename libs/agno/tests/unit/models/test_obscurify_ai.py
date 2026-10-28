import os
from unittest.mock import patch

import pytest

from agno.exceptions import ModelAuthenticationError
from agno.models.obscurify_ai import ObscurifyAI
from agno.models.utils import get_model, get_model_from_dict


def test_obscurify_ai_initialization_with_api_key():
    model = ObscurifyAI(id="z-ai/glm-5.3", api_key="test-api-key")
    assert model.id == "z-ai/glm-5.3"
    assert model.api_key == "test-api-key"
    assert model.base_url == "https://obscurify.ai/v1"


def test_obscurify_ai_initialization_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        model = ObscurifyAI(id="z-ai/glm-5.3")
        client_params = None
        with pytest.raises(ModelAuthenticationError):
            client_params = model._get_client_params()
        assert client_params is None


def test_obscurify_ai_initialization_with_env_api_key():
    with patch.dict(os.environ, {"OBSCURIFY_API_KEY": "env-api-key"}):
        model = ObscurifyAI(id="z-ai/glm-5.3")
        assert model.api_key == "env-api-key"


def test_obscurify_ai_client_params():
    model = ObscurifyAI(id="z-ai/glm-5.3", api_key="test-api-key")
    client_params = model._get_client_params()
    assert client_params["api_key"] == "test-api-key"
    assert client_params["base_url"] == "https://obscurify.ai/v1"


def test_obscurify_ai_default_values():
    model = ObscurifyAI(api_key="test-api-key")
    assert model.id == "deepseek/deepseek-v4-flash"
    assert model.name == "Obscurify.ai"
    assert model.provider == "Obscurify.ai"


def test_obscurify_ai_resolves_from_string_syntax():
    model = get_model("obscurify-ai:z-ai/glm-5.3")
    assert isinstance(model, ObscurifyAI)
    assert model.id == "z-ai/glm-5.3"


def test_obscurify_ai_round_trips_through_dict():
    model = ObscurifyAI(id="z-ai/glm-5.3", api_key="test-api-key")
    rebuilt = get_model_from_dict(model.to_dict())
    assert isinstance(rebuilt, ObscurifyAI)
    assert rebuilt.id == "z-ai/glm-5.3"
