# RAG ChatBot example

This is a simple example to showcase how a ChatBot can be made that can answer questions based on data that is provided by us later ie. not during the training of the llm.

## Providers

Currently, there are 2 providers for LLMs. These are OpenAI and HuggingFace (HF). But this can easily be changed. Visit [langchain's docs](https://python.langchain.com/docs/get_started/introduction) to see which other providers can be used.

## Usage

- Acquire and set required API keys in the environment variables according to which model you want to use. For example, set `OPENAI_API_KEY` if you want to use OpenAI's llm (by running `using_openai.py`).
- Install required dependencies using `poetry` or by creating a virtual environment maunally and installing the dependencies using `pip`.
- Run the file you want (either `using_openai.py` or `using_hf.py`).

## Example Questions

Here are a few questions asked to the bot along with the answers that the bot gave.

- What is the IDDDP programme?
  Ans: The IDDDP program is a program that allows undergraduate students from B.S., B.Tech. and DD (B.Tech.+M.Tech.)
  programmes to apply for a Dual Degree (DD) and M.Tech. programme at the end of their sixth semester. The
  programme requires students to complete 8-9 courses of 6 credits and a DD/M.Tech. project (DDP/MTP) of 74 - 92
  credits.

- How is CPI calculated?
  Ans: The CPI is calculated by taking the sum of the credits multiplied by the grade points for all courses registered by the student since they entered the institute and dividing it by the total sum of the credits for all the courses registered. The CPI is calculated to two decimal places. It will reflect failed status in case of an FR grade until the course is cleared. When the course is cleared by obtaining a pass grade on subsequent registrations, the CPI will only reflect the new grade and not the fail grade earned earlier.

- Can a person leave their course earlier?
  Ans: Yes, a B.Tech. or B.S. student can apply to leave the Institute at the end of an academic semester if their credit requirements are met and they have spent at least three years in the Institute.

- How many minors can a person do in their entire course?
  Ans: A person can do two minors if their time table permits. However, they should discuss this with their faculty adviser since completing two minors would involve a significant overload.

- Can a person do both NCC and NSS?
  Ans: Yes, a person can do both NCC and NSS as long as they register for one at the beginning of the first two
  semesters. They are also allowed to take NSS/NSO/NCC in subsequent years if they have a special interest.

:warning: **NOTE:** The answers given above are generated using OpenAI's LLMs though, you can use others from HuggingFace by running the file `using_hf.py` and changing the `repo_id` in the model creation part.
