import gradio as gr
from utils.file_handler import load_csv
from utils.query_processor import process_query
from utils.llm_handler import query_llm
from utils.visualization import plot_graph

df = None

def handle_csv(file):
    global df
    df = load_csv(file)
    return "CSV uploaded successfully!"

def handle_query(user_input):
    if df is None:
        return "Please upload a CSV first."
    query = process_query(user_input, df)
    response = query_llm(query.question)
    return response

def handle_plot(x_col, y_col, graph_type):
    if df is None:
        return "Please upload a CSV first."
    return plot_graph(df, x_col, y_col, graph_type)

with gr.Blocks() as app:
    gr.Markdown("# CSV Question Answering & Visualization App")
    
    file_upload = gr.File(label="Upload CSV", type="file")
    file_upload.upload(handle_csv, file_upload, None)
    
    query_input = gr.Textbox(label="Ask a question")
    query_output = gr.Textbox(label="Answer")
    query_button = gr.Button("Get Answer")
    query_button.click(handle_query, query_input, query_output)

    col_x = gr.Textbox(label="X-axis Column")
    col_y = gr.Textbox(label="Y-axis Column")
    graph_type = gr.Radio(["line", "bar", "scatter"], label="Graph Type")
    graph_output = gr.Image(label="Graph")
    graph_button = gr.Button("Generate Graph")
    graph_button.click(handle_plot, [col_x, col_y, graph_type], graph_output)

app.launch()
