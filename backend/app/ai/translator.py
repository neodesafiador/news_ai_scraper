"""
AI-powered translation to simple Japanese using LangChain and OpenAI
"""
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os
import logging

logger = logging.getLogger(__name__)


class ArticleTranslator:
    """Translate articles to simple Japanese using GPT"""

    def __init__(self, model: str = "gpt-4", temperature: float = 0.3):
        """
        Initialize the translator

        Args:
            model: OpenAI model to use
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

    def translate_title(self, title: str) -> Optional[str]:
        """
        Translate article title to Japanese

        Args:
            title: English title

        Returns:
            Japanese title
        """
        try:
            system_prompt = """You are an expert translator specializing in AI and technology news.
Translate English article titles to natural, engaging Japanese.

Guidelines:
- Make it catchy and informative
- Use appropriate technical terms in Japanese
- Keep it concise (under 60 characters)
- Sound natural to Japanese readers"""

            human_prompt = f"Translate this article title to Japanese:\n\n{title}"

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]

            response = self.llm.invoke(messages)
            translated_title = response.content.strip()

            logger.info(f"Translated title: {title[:50]}...")
            return translated_title

        except Exception as e:
            logger.error(f"Error translating title: {str(e)}")
            return None

    def translate_summary(self, summary: str) -> Optional[str]:
        """
        Translate article summary to simple Japanese

        Args:
            summary: English summary

        Returns:
            Japanese summary
        """
        try:
            system_prompt = """You are an expert translator specializing in AI and technology content.
Translate English summaries into clear, easy-to-understand Japanese (やさしい日本語).

Guidelines:
- Use simple, accessible Japanese suitable for a general audience
- Break down complex technical concepts into understandable language
- Maintain accuracy while prioritizing clarity
- Use appropriate technical terms when necessary, with explanations
- Keep the tone informative but friendly
- Aim for 150-200 characters in Japanese"""

            human_prompt = f"""Translate this article summary to easy-to-understand Japanese:

{summary}

Make it accessible for readers who may not be technical experts."""

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]

            response = self.llm.invoke(messages)
            translated_summary = response.content.strip()

            logger.info("Successfully translated summary to Japanese")
            return translated_summary

        except Exception as e:
            logger.error(f"Error translating summary: {str(e)}")
            return None

    def translate_key_points(self, key_points: List[str]) -> Optional[List[str]]:
        """
        Translate key points to Japanese with explanations

        Args:
            key_points: List of English key points

        Returns:
            List of Japanese key points with explanations
        """
        try:
            # Join key points into a single text
            key_points_text = '\n'.join([f"{i+1}. {point}" for i, point in enumerate(key_points)])

            system_prompt = """You are an expert translator specializing in AI and technology content.
Translate key points into clear Japanese with helpful context.

Guidelines:
- Use simple, accessible Japanese (やさしい日本語)
- Add brief explanations for technical terms
- Make each point self-contained and clear
- Keep each point concise (under 100 characters)
- Use 「」for quotations and emphasis
- Maintain the informative value while being accessible"""

            human_prompt = f"""Translate these key points to easy-to-understand Japanese:

{key_points_text}

Provide the translation as a numbered list. Add brief explanations for technical terms where helpful."""

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]

            response = self.llm.invoke(messages)
            translated_text = response.content.strip()

            # Parse back into list
            translated_points = []
            for line in translated_text.split('\n'):
                line = line.strip()
                if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
                    # Remove numbering
                    point = line.lstrip('0123456789.-•) ').strip()
                    if point:
                        translated_points.append(point)

            logger.info(f"Translated {len(translated_points)} key points to Japanese")
            return translated_points

        except Exception as e:
            logger.error(f"Error translating key points: {str(e)}")
            return None

    def translate_article(self, title: str, summary: str, key_points: List[str]) -> Optional[dict]:
        """
        Translate complete article (title, summary, and key points)

        Args:
            title: English title
            summary: English summary
            key_points: List of English key points

        Returns:
            Dictionary with translated content
        """
        try:
            translated_title = self.translate_title(title)
            translated_summary = self.translate_summary(summary)
            translated_key_points = self.translate_key_points(key_points)

            if not all([translated_title, translated_summary, translated_key_points]):
                logger.error("Failed to translate some components")
                return None

            return {
                'title_ja': translated_title,
                'summary_ja': translated_summary,
                'key_points_ja': translated_key_points
            }

        except Exception as e:
            logger.error(f"Error translating article: {str(e)}")
            return None
