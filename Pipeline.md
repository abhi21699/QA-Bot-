# Basic pipeline of how the things will progress . ( Will add more details as we proceed)

1) Let's start with you uploading a PDF file to the system.
2) The text content from all the pages in that PDF is then extracted and separated into smaller, more manageable chunks.
3) Each of those text chunks is converted into a numerical representation called a vector embedding, which captures the meaning and context of the text.
4) These vector embeddings are stored in a special database that allows for efficient similarity searches.
5) When you enter a question related to the PDF content, the system finds the text chunks with embeddings most similar to your query.
6) Those relevant chunks are then fed into a language model, which uses them to generate a coherent and accurate response to your original question.