# camelot的优点是代码简洁，但效果却有点粗糙。如果PDF文档的内容结构清晰，则用pdfplumber转成Excel的效果更好
import camelot


tables = camelot.read_pdf('documents/2024-2025学年深圳市罗湖区幼儿园办学基本信息表.pdf', pages='all')
tables.export('documents/幼儿园camelot.xlsx', f='excel')

