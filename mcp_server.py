from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document given its name."
)
def read_document(
    doc_id: Annotated[str, Field(description="The id of the document to read.")]
):
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    return docs[doc_id]


@mcp.tool(
    name="edit_doc_contents",
    description="Edit the contents of a document given its name and new content."
)
def edit_document(
    doc_id: Annotated[str, Field(description="The id of the document to edit.")],
    new_content: Annotated[str, Field(description="The new content for the document.")]
):
    if doc_id not in docs:
        raise ValueError(f"Document with id '{doc_id}' not found.")
    docs[doc_id] = new_content
    return f"Document '{doc_id}' updated successfully."


if __name__ == "__main__":
    mcp.run(transport="stdio")