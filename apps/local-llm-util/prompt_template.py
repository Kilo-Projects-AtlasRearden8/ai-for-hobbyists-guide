"""Print a safe, fill-in-the-blanks prompt template for hobby projects."""

TEMPLATE = """{role}

{task}

Context: {context}

Format: {format}

Remember: never paste personal info into an AI tool. Use placeholders like
[YOUR CITY], [MY NAME], or [ITEM] instead of real names, addresses, phone
numbers, emails, passwords, bank details, or health information.
"""


def main():
    print(TEMPLATE.format(
        role="Act like a patient hobby teacher.",
        task="Describe what you want in one or two sentences.",
        context="I am a beginner. Keep language simple and encouraging.",
        format="Use a bulleted list. Keep each step under two sentences.",
    ))
    print("Copy the prompt above into your AI chat, then fill in the blanks.")


if __name__ == "__main__":
    main()
