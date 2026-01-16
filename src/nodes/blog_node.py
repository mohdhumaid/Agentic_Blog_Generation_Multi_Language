from src.states.blogstate import BlogState, Blog
from langchain_core.messages import HumanMessage, SystemMessage
import json
from pydantic import ValidationError



import json
import re

def safe_json_parse(text: str) -> dict:
    if not text:
        raise ValueError("LLM returned empty response")

    # Remove code fences if present
    text = text.strip()
    text = re.sub(r"^```json|```$", "", text, flags=re.MULTILINE).strip()

    # Extract first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON object found in response:\n{text}")

    return json.loads(match.group())

class BlogNode:
    """
    A class to represent he blog node
    """

    def __init__(self,llm):
        self.llm=llm

    
    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly

                   """
            
            sytem_message=prompt.format(topic=state["topic"])
            print(sytem_message)
            response=self.llm.invoke(sytem_message)
            print(response)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
        



    def translation11(self, state: BlogState) -> BlogState:
        language = state["current_language"]

        messages = [
            (
                "system",
                f"""
                    You are a translator.
                    Translate the blog into {language}.
                    Return ONLY valid JSON.
                    No markdown.
                    No explanations.

                    JSON schema:
                    {{
                    "title": string,
                    "content": string
                    }}
                """.strip(),
            ),
            (
                "human",
                f"Title:{state['blog'].title},Content:{state['blog'].content}",
            ),
        ]

        response = self.llm.invoke(messages)

        try:
            data = json.loads(response.content)
            blog = Blog(**data)
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Translation parsing failed: {e}")

        return {
            **state,
            "blog": blog,
        }

    
    def translation(self, state: BlogState):
        """
        Translate the blog into the specified target language.
        Always returns strict JSON.
        """

        target_language = state["current_language"]

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a professional translation engine.\n"
                    f"Translate the given blog into {target_language}.\n"
                    "Maintain tone, structure, and formatting.\n"
                    "Return ONLY valid JSON in the format:\n"
                    "{ \"title\": string, \"content\": string }"
                )
            },
            {
                "role": "user",
                "content": f"""
    Title:
    {state['blog']['title']}

    Content:
    {state['blog']['content']}
    """
            }
        ]

        response = self.llm.invoke(messages)

        translated = safe_json_parse(response.content)

        return {
            **state,
            "blog": {
                "title": translated["title"],
                "content": translated["content"]
            }
        }


    def route(self, state: BlogState):
        return {"current_language": state['current_language'] }
    

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french": 
            return "french"
        else:
            return state['current_language']