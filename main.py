# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from agent.agentic_workflow import GraphBuilder
# from utils.save_to_document import save_document
# from starlette.responses import JSONResponse
# import os
# import datetime
# from dotenv import load_dotenv
# from pydantic import BaseModel
# load_dotenv()

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # set specific origins in prod
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# class QueryRequest(BaseModel):
#     question: str

# @app.post("/query")
# async def query_travel_agent(query:QueryRequest):
#     try:
#         print(query)
#         graph = GraphBuilder(model_provider="groq")
#         react_app=graph()
#         #react_app = graph.build_graph()

#         png_graph = react_app.get_graph().draw_mermaid_png()
#         with open("my_graph.png", "wb") as f:
#             f.write(png_graph)

#         print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
#         # Assuming request is a pydantic object like: {"question": "your text"}
#         messages={"messages": [query.question]}
#         output = react_app.invoke(messages)

#         # If result is dict with messages:
#         if isinstance(output, dict) and "messages" in output:
#             final_output = output["messages"][-1].content  # Last AI response
#         else:
#             final_output = str(output)
        
#         return {"answer": final_output}
#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e)})

# main.py (UPDATED WITHOUT AUTH)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from pydantic import BaseModel
import os
import datetime
import logging
from dotenv import load_dotenv
from utils.pdf_generator import generate_pdf  # New import

# Load env and configure logging
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Travel Planner API",
    description="An intelligent travel planning assistant",
    version="1.0.0"
)

# Allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    timestamp: str
    status: str = "success"

@app.get("/")
async def root():
    return {"message": "AI Travel Planner API is running!", "timestamp": datetime.datetime.now().isoformat()}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}

@app.post("/query", response_model=QueryResponse)
async def query_travel_agent(query: QueryRequest):
    try:
        logger.info(f"Received query: {query.question}")

        if not query.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")

        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        try:
            png_graph = react_app.get_graph().draw_mermaid_png()
            with open("my_graph.png", "wb") as f:
                f.write(png_graph)
        except Exception as e:
            logger.warning(f"Graph generation skipped: {str(e)}")

        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return QueryResponse(
            answer=final_output,
            timestamp=datetime.datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



@app.post("/download")
async def download_pdf():
    try:
        # Make sure this file path is correct and the file actually exists
        latest_pdf = max([os.path.join("pdfs", f) for f in os.listdir("pdfs") if f.endswith(".pdf")], key=os.path.getctime)
        return FileResponse(path=latest_pdf, media_type="application/pdf", filename=os.path.basename(latest_pdf))
    except Exception as e:
        print(f"Download error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate or fetch PDF.")

