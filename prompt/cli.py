import click
from os import path, makedirs, getenv
import openai
from rich.progress import Console
import json
import readline

console = Console()


def configure_openai():
    config_file = path.expanduser("~/.openai/config.json")
    if not path.exists(config_file):
        makedirs(path.dirname(config_file), exist_ok=True)
        api_key = input("🔑 Enter your OpenAI API key: ")
        with open(config_file, "w", encoding="UTF-8") as f:
            f.write(f'{{"api_key": "{api_key}"}}')
    else:
        with open(config_file, "r", encoding="UTF-8") as f:
            api_key = json.load(f).get("api_key")
        if not api_key:
            api_key = input("🔑 Enter your OpenAI API key: ")
            with open(config_file, "w", encoding="UTF-8") as f:
                f.write(f'{{"api_key": "{api_key}"}}')
    openai.api_key = api_key or getenv("OPENAI_API_KEY")


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(version="2.1.0")
@click.option("--clear", is_flag=True, help="🌊 Clear the context each round of chat")
@click.option("--model", default="gpt-3.5-turbo", help="🔄 The OpenAI model type.")
def cli(ctx, clear, model):
    """🥝 A command line application to interact with OpenAI's ChatGPT."""
    if not ctx.invoked_subcommand:
        configure_openai()
        session_data = []
        click.echo("")
        click.echo(" Session started. Enter 'exit' to end the session.")
        while True:
            user_input = click.prompt("➡ ")
            session_data.append({"role": "user", "content": user_input})
            if user_input.lower() == "exit":
                break
            try:
                with console.status("Waiting for chatgpt...", spinner="dots8Bit"):
                    completion = openai.ChatCompletion.create(
                        model=model, messages=session_data
                    )
                    print("")
                    print(completion["choices"][0]["message"]["content"])
                    print("")
                    session_data.append(
                        {
                            "role": "system",
                            "content": completion["choices"][0]["message"]["content"],
                        }
                    )
                    if clear:
                        session_data = []
            except openai.error.AuthenticationError():
                print("🔒 Authentication Failed. Try with a fresh API key.")
                break
            except Exception:
                print(
                    "❌ Failed to get reply from chatGPT. Please try again with a different prompt or check your api key quota."
                )
                break


@cli.command("update")
def update_key():
    """🔐 Update the OpenAI API key."""
    config_file = path.expanduser("~/.openai/config.json")
    api_key = input("Enter your OpenAI API key: ")
    if not path.exists(config_file):
        makedirs(path.dirname(config_file), exist_ok=True)

    with open(config_file, "w", encoding="UTF-8") as f:
        f.write(f'{{"api_key": "{api_key}"}}')
    print("API key updated successfully!")
