import base64
import json
from pathlib import Path

import pytest
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice
from openai.types.completion_usage import CompletionUsage

from concurrent_openai.types import CompletionResponse


@pytest.fixture
def mocked_chat_completion() -> ChatCompletion:
    return ChatCompletion(
        id="chatcmpl-99XUGZR68HIAcvljfTyb5FYAxxtJH",
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content="Hello! How can I assist you today?",
                    role="assistant",
                    function_call=None,
                    tool_calls=None,
                ),
            )
        ],
        created=1712060704,
        model="gpt-4-0613",
        object="chat.completion",
        system_fingerprint=None,
        usage=CompletionUsage(completion_tokens=9, prompt_tokens=10, total_tokens=19),
    )


@pytest.fixture
def mocked_process_completion_requests_response() -> CompletionResponse:
    return CompletionResponse(
        api_response=ChatCompletion(
            id="chatcmpl-9ALGtGXZDpuqlZhEfeEz7fUGKb8zK",
            choices=[
                Choice(
                    finish_reason="stop",
                    index=0,
                    logprobs=None,
                    message=ChatCompletionMessage(
                        content="Emoji with sunglasses.",
                        role="assistant",
                        function_call=None,
                        tool_calls=None,
                    ),
                )
            ],
            created=1712252075,
            model="gpt-4-1106-vision-preview",
            object="chat.completion",
            system_fingerprint=None,
            usage=CompletionUsage(
                completion_tokens=4, prompt_tokens=282, total_tokens=286
            ),
        ),
        answer="Emoji with sunglasses.",
        estimated_prompt_tokens=295,
        prompt_tokens=282,
        completion_tokens=4,
        total_cost=0.00147,
        conversation_id="chatcmpl-9ALGtGXZDpuqlZhEfeEz7fUGKb8zK",
    )


@pytest.fixture
def data_dir() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def conversation1(data_dir: Path) -> list[dict[str, str]]:
    with open(data_dir / "conversation1.json") as f:
        return json.load(f)


@pytest.fixture
def conversation2(data_dir: Path) -> list[dict[str, str]]:
    with open(data_dir / "conversation2.json") as f:
        return json.load(f)


@pytest.fixture
def base64_sunglasses_image(data_dir: Path) -> str:
    with open(data_dir / "sunglasses.png", "rb") as f:
        image = f.read()
    base64_image = base64.b64encode(image).decode("utf-8")
    return f"data:image/png;base64,{base64_image}"
