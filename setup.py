from setuptools import setup, find_packages
setup(
    name='prompt-creator',
    version='1.1.0',
    packages=find_packages(),
    author='Your Name',  # نام خود را اینجا وارد کنید
    author_email='your.email@example.com',  # ایمیل خود را اینجا وارد کنید
    description='A tool to create prompts from project files based on specified rules.',
    long_description=open('Readme.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KhtaAi/Prompt-Creator-from-projects',
    entry_points={
        'console_scripts': [
            'prompt-creator=prompt_creator.main:run',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)