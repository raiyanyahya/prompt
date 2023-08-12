[![Actions Status](https://github.com/raiyanyahya/prompt/workflows/Build%20Test/badge.svg)](https://github.com/raiyanyahya/prompt/actions) [![Actions Status](https://github.com/raiyanyahya/prompt/workflows/Package%20Release/badge.svg)](https://github.com/raiyanyahya/prompt/actions) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=raiyanyahya_prompt&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=raiyanyahya_prompt) [![CodeQL](https://github.com/raiyanyahya/prompt/workflows/CodeQL/badge.svg)](https://github.com/raiyanyahya/prompt/actions?query=workflow%3ACodeQL) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/05a21e6c4ed4494ba39e2ee43b2327d2)](https://www.codacy.com/gh/raiyanyahya/prompt/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=raiyanyahya/prompt&amp;utm_campaign=Badge_Grade) [![](https://img.shields.io/badge/python-3.6+-blue.svg)]

# Prompt 🥝 - A ChatGPT CLI

![](https://gifyu.com/images/demo.gif)

`prompt` is designed to provide users a command-line interface for the ChatGPT API, which uses OpenAI's GPT language model to generate text based on user input.

The application helps you start a `session` with ChatGPT so that the `context` is preserved and longer conversions with contexts are considered. The user's prompts and the responses are sent back to ChatGPT everytime.

The ChatGPT api usage depends on the number of tokens used and it is important that you use the tokens wisely. After a prompt has been answered the application will resend the last prompt and answer in the next prompt, this makes sure you can have a continued conversion with ChatGPT ` much like using ChatGPT in a single chat session `. This makes the token count larger and larger as you continue to chat. If you are not concerned with context use the `--clear` flag which will save your token usage. Use the `model` option to add 

I hope you find it useful.


## Configuration

The application requires you to have an api token to query the OpenAI's ChatGPT api. You can read about and get it here https://platform.openai.com/account/api-keys .

## Installation

Install the prompt python package directly from pypi. 

```console
  pip install promptcli
```
I would recommend using pipx instead of pip to install cli applications on you machine.

## Usage

```console
Usage: prompt [OPTIONS] COMMAND [ARGS]...

  🥝 A command line application to interact with OpenAI's ChatGPT.

Options:
  --version     Show the version and exit.
  --clear    🌊 Clear the context each round of chat
  --model    🔄 The OpenAI model type.
  --help        Show this message and exit.

Commands:
  update  🔐 Update the OpenAI API key.
```


Please feel to create issues or request for features. More options and commands will be added to the application in the near future.
