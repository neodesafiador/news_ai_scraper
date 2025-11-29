"""
AI-powered article summarization using LangChain and OpenAI
"""
from typing import Dict, Optional
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
import os
import logging

logger = logging.getLogger(__name__)


class ArticleSummarizer:
    """Summarize English articles using GPT"""

    def __init__(self, model: str = "gpt-4", temperature: float = 0.3):
        """
        Initialize the summarizer

        Args:
            model: OpenAI model to use (gpt-4, gpt-3.5-turbo, etc.)
            temperature: Sampling temperature (0-1)
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            openai_api_key=api_key
        )

    def summarize(self, title: str, content: str) -> Optional[str]:
        """
        Summarize an article

        Args:
            title: Article title
            content: Article content

        Returns:
            Summarized text in English
        """
        try:
            system_prompt = """You are an expert at summarizing technical articles about AI and technology.
Your task is to create a concise, accurate summary that captures the key points of the article.

Guidelines:
- Focus on the main findings, innovations, or news
- Keep the summary between 100-150 words
- Maintain technical accuracy
- Use clear, accessible language
- Preserve important facts, numbers, and names"""

            human_prompt = f"""Please summarize the following article:

Title: {title}

Content: {content[:4000]}  # Limit content length

Provide a concise summary in English."""

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]

            response = self.llm.invoke(messages)
            summary = response.content.strip()

            logger.info(f"Successfully summarized: {title[:50]}...")
            return summary

        except Exception as e:
            logger.error(f"Error summarizing article: {str(e)}")
            return None

    def extract_key_points(self, title: str, content: str) -> Optional[list]:
        """
        Extract key points from an article

        Args:
            title: Article title
            content: Article content

        Returns:
            List of key points in English
        """
        try:
            system_prompt = """You are an expert at analyzing technical articles about AI and technology.
Your task is to extract the most important key points from the article.

Guidelines:
- Identify 3-5 key takeaways
- Each point should be one clear sentence
- Focus on actionable insights, findings, or implications
- Prioritize unique or newsworthy information"""

            human_prompt = f"""Please extract the key points from the following article:

Title: {title}

Content: {content[:4000]}

Provide 3-5 key points as a numbered list. Each point should be a single sentence."""

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]

            response = self.llm.invoke(messages)
            key_points_text = response.content.strip()

            # Parse the numbered list into an array
            key_points = []
            for line in key_points_text.split('\n'):
                line = line.strip()
                # Remove numbering (1., 2., etc.)
                if line and (line[0].isdigit() or line.startswith('-')):
                    # Remove the number/bullet and clean
                    point = line.lstrip('0123456789.-) ').strip()
                    if point:
                        key_points.append(point)

            logger.info(f"Extracted {len(key_points)} key points from: {title[:50]}...")
            return key_points[:5]  # Limit to 5 points

        except Exception as e:
            logger.error(f"Error extracting key points: {str(e)}")
            return None
