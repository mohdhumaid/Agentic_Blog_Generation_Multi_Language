from langgraph.graph import StateGraph,START,END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Built a graph to generate a blog based on topic
        """
        self.blog_node_obj=BlogNode(self.llm)

        ##Nodes
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)

        return self.graph
    def build_language_graph(self):
        """
        Built a graph for blog generation with input topic and language
        """
        self.blog_node_obj = BlogNode(self.llm)

        ## Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        # Existing + English
        self.graph.add_node(
            "english_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "english"})
        )
        self.graph.add_node(
            "hindi_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "hindi"})
        )
        self.graph.add_node(
            "french_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "french"})
        )
        self.graph.add_node(
            "spanish_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "spanish"})
        )
        self.graph.add_node(
            "german_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "german"})
        )
        self.graph.add_node(
            "italian_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "italian"})
        )
        self.graph.add_node(
            "portuguese_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "portuguese"})
        )
        self.graph.add_node(
            "arabic_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "arabic"})
        )
        self.graph.add_node(
            "chinese_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "chinese"})
        )
        self.graph.add_node(
            "japanese_translation",
            lambda state: self.blog_node_obj.translation({**state, "current_language": "japanese"})
        )

        self.graph.add_node("route", self.blog_node_obj.route)

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        ## Conditional edges
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "english": "english_translation",
                "hindi": "hindi_translation",
                "french": "french_translation",
                "spanish": "spanish_translation",
                "german": "german_translation",
                "italian": "italian_translation",
                "portuguese": "portuguese_translation",
                "arabic": "arabic_translation",
                "chinese": "chinese_translation",
                "japanese": "japanese_translation"
            }
        )

        ## End edges
        self.graph.add_edge("english_translation", END)
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)
        self.graph.add_edge("spanish_translation", END)
        self.graph.add_edge("german_translation", END)
        self.graph.add_edge("italian_translation", END)
        self.graph.add_edge("portuguese_translation", END)
        self.graph.add_edge("arabic_translation", END)
        self.graph.add_edge("chinese_translation", END)
        self.graph.add_edge("japanese_translation", END)

        return self.graph

    def setup_graph(self, usecase):
        if usecase=="topic":
            self.build_topic_graph()
        if usecase=="language":
            self.build_language_graph()

        return self.graph.compile()
    


## below code is for LangSmith LangGraph Studio Debugg
llm=GroqLLM().get_llm()

#Get the graph
graph_builder=GraphBuilder(llm)
graph=graph_builder.build_language_graph().compile()