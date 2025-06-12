import os, pymupdf , asyncio
from llama_cloud_services import LlamaParse
from dotenv import load_dotenv
load_dotenv(dotenv_path="./python_worker/.env")


parser = LlamaParse(
   api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
    num_workers=4,
    verbose=True,
    language="en",
)

'''
path ='././Temp/'
print(path)
isExist = os.path.exists(path)
print(isExist)
'''

async def read_pdf_llama(file_path:str):
    result = await parser.aparse(file_path)
    if not result:return "parser llama failed"
    text_document = result.get_text_documents(split_by_page=True)
    with open("././Temp/output_from_llama.txt", "wb") as out:
        for doc in text_document:
            out.write(doc.text.encode("utf-8"))
            out.write(bytes((12,)))
            return None
        return None


async def read_pdf_pymupdf(file_path:str):
    doc = pymupdf.open(file_path)
    if not doc: return "parser pymupdf failed"
    out= open("././Temp/output_from_pymupdf.txt", "wb")
    for page in doc:
        text = page.get_text().encode("utf8")
        out.write(text)
        out.write(bytes((12,)))
    out.close()


if __name__ == "__main__":
    output_llama= asyncio.run(read_pdf_llama("./Temp/Resume latest.pdf"))
    output_pymupdf= asyncio.run(read_pdf_pymupdf("./Temp/AmanProfResume.docx.pdf"))