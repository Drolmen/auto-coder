import argparse
from autocoder.common import AutoCoderArgs
from autocoder.lang import lang_desc
import locale
from typing import Optional,List


def parse_args(input_args:Optional[List[str]]=None) -> AutoCoderArgs:
    system_lang, _ = locale.getdefaultlocale()
    lang = "zh" if system_lang and system_lang.startswith("zh") else "en"
    desc = lang_desc[lang]

    parser = argparse.ArgumentParser(description=desc["parser_desc"])
    subparsers = parser.add_subparsers(dest="command")

    parser.add_argument("--source_dir", required=False, help=desc["source_dir"])
    parser.add_argument("--git_url", help=desc["git_url"])
    parser.add_argument("--target_file", required=False, help=desc["target_file"])
    parser.add_argument("--query", help=desc["query"])
    parser.add_argument("--template", default="common", help=desc["template"])
    parser.add_argument("--project_type", default="py", help=desc["project_type"])
    parser.add_argument("--execute", action="store_true", help=desc["execute"])
    parser.add_argument("--package_name", default="", help=desc["package_name"])
    parser.add_argument("--script_path", default="", help=desc["script_path"])

    parser.add_argument("--model", default="", help=desc["model"])
    parser.add_argument(
        "--model_max_length", type=int, default=2000, help=desc["model_max_length"]
    )
    parser.add_argument(
        "--model_max_input_length",
        type=int,
        default=6000,
        help=desc["model_max_input_length"],
    )

    parser.add_argument("--vl_model", default="", help=desc["vl_model"])
    parser.add_argument("--sd_model", default="", help=desc["sd_model"])
    parser.add_argument("--emb_model", default="", help=desc["emb_model"])

    parser.add_argument("--index_model", default="", help=desc["index_model"])
    parser.add_argument(
        "--index_model_max_length",
        type=int,
        default=0,
        help=desc["index_model_max_length"],
    )
    parser.add_argument(
        "--index_model_max_input_length",
        type=int,
        default=0,
        help=desc["index_model_max_input_length"],
    )
    parser.add_argument(
        "--index_model_anti_quota_limit",
        type=int,
        default=0,
        help=desc["index_model_anti_quota_limit"],
    )
    parser.add_argument(
        "--index_filter_level", type=int, default=0, help=desc["index_filter_level"]
    )
    parser.add_argument(
        "--index_filter_workers", type=int, default=1, help=desc["index_filter_workers"]
    )
    parser.add_argument(
        "--index_build_workers", type=int, default=1, help=desc["index_build_workers"]
    )

    parser.add_argument("--file", default=None, required=False, help=desc["file"])
    parser.add_argument("--ray_address", default="auto", help=desc["ray_address"])
    parser.add_argument(
        "--anti_quota_limit", type=int, default=1, help=desc["anti_quota_limit"]
    )
    parser.add_argument(
        "--skip_build_index", action="store_false", help=desc["skip_build_index"]
    )
    parser.add_argument(
        "--print_request", action="store_true", help=desc["print_request"]
    )
    parser.add_argument("--code_model", default="", help=desc["code_model"])
    parser.add_argument("--planner_model", default="", help=desc["planner_model"])
    parser.add_argument(
        "--py_packages", required=False, default="", help=desc["py_packages"]
    )
    parser.add_argument(
        "--human_as_model", action="store_true", help=desc["human_as_model"]
    )
    parser.add_argument("--urls", default="", help=desc["urls"])
    parser.add_argument(
        "--urls_use_model", action="store_true", help=desc["urls_use_model"]
    )
    parser.add_argument("--exclude_files", default="", help="")
    parser.add_argument("--query_prefix", default=None, help=desc["query_prefix"])
    parser.add_argument("--query_suffix", default=None, help=desc["query_suffix"])

    parser.add_argument("--search", default="", help="")
    parser.add_argument("--search_engine", default="", help=desc["search_engine"])
    parser.add_argument(
        "--search_engine_token", default="", help=desc["search_engine_token"]
    )

    parser.add_argument(
        "--enable_rag_search",
        nargs="?",
        const=True,
        default=False,
        help=desc["enable_rag_search"],
    )
    parser.add_argument(
        "--enable_rag_context",
        nargs="?",
        const=True,
        default=False,
        help=desc["enable_rag_context"],
    )

    parser.add_argument("--rag_token", default="", help="")
    parser.add_argument("--rag_url", default="", help="")

    parser.add_argument(
        "--auto_merge", nargs="?", const=True, default=False, help=desc["auto_merge"]
    )

    parser.add_argument("--image_file", default="", help=desc["image_file"])
    parser.add_argument("--image_mode", default="direct", help=desc["image_mode"])
    parser.add_argument(
        "--image_max_iter", type=int, default=1, help=desc["image_max_iter"]
    )

    parser.add_argument(
        "--enable_multi_round_generate",
        action="store_true",
        help=desc["enable_multi_round_generate"],
    )
    parser.add_argument(
        "--skip_confirm", action="store_true", help=desc["skip_confirm"]
    )

    revert_parser = subparsers.add_parser("revert", help=desc["revert_desc"])
    revert_parser.add_argument("--file", help=desc["revert_desc"])

    store_parser = subparsers.add_parser("store", help=desc["store_desc"])
    store_parser.add_argument("--source_dir", default=".", help=desc["source_dir"])
    store_parser.add_argument("--ray_address", default="auto", help=desc["ray_address"])

    index_parser = subparsers.add_parser("index", help=desc["index_desc"])
    index_parser.add_argument("--file", help=desc["file"])
    index_parser.add_argument("--model", default="", help=desc["model"])
    index_parser.add_argument("--index_model", default="", help=desc["index_model"])
    index_parser.add_argument("--source_dir", required=False, help=desc["source_dir"])
    index_parser.add_argument("--project_type", default="py", help=desc["project_type"])
    index_parser.add_argument("--ray_address", default="auto", help=desc["ray_address"])

    index_query_parser = subparsers.add_parser(
        "index-query", help=desc["index_query_desc"]
    )  # New subcommand
    index_query_parser.add_argument("--file", help=desc["file"])
    index_query_parser.add_argument("--model", default="", help=desc["model"])
    index_query_parser.add_argument(
        "--index_model", default="", help=desc["index_model"]
    )
    index_query_parser.add_argument(
        "--source_dir", required=False, help=desc["source_dir"]
    )
    index_query_parser.add_argument("--query", help=desc["query"])
    index_query_parser.add_argument(
        "--index_filter_level", type=int, default=2, help=desc["index_filter_level"]
    )
    index_query_parser.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )

    doc_parser = subparsers.add_parser("doc", help=desc["doc_desc"])
    doc_parser.add_argument("--urls", default="", help=desc["urls"])
    doc_parser.add_argument("--model", default="", help=desc["model"])
    doc_parser.add_argument("--target_file", default="", help=desc["target_file"])
    doc_parser.add_argument("--file", default="", help=desc["file"])
    doc_parser.add_argument("--source_dir", required=False, help=desc["source_dir"])
    doc_parser.add_argument(
        "--human_as_model", action="store_true", help=desc["human_as_model"]
    )
    doc_parser.add_argument(
        "--urls_use_model", action="store_true", help=desc["urls_use_model"]
    )
    doc_parser.add_argument("--ray_address", default="auto", help=desc["ray_address"])

    doc_subparsers = doc_parser.add_subparsers(dest="doc_command")
    doc_build_parse = doc_subparsers.add_parser("build", help="")
    doc_build_parse.add_argument("--source_dir", default="", help="")
    doc_build_parse.add_argument("--model", default="", help=desc["model"])
    doc_build_parse.add_argument("--emb_model", default="", help=desc["emb_model"])
    doc_build_parse.add_argument("--file", default="", help=desc["file"])
    doc_build_parse.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )
    doc_build_parse.add_argument(
        "--required_exts", default="", help=desc["doc_build_parse_required_exts"]
    )
    doc_build_parse.add_argument(
        "--collection", default="default", help="Collection name for indexing"
    )
    doc_build_parse.add_argument(
        "--description", default="", help="Description of the indexed content"
    )

    doc_query_parse = doc_subparsers.add_parser("query", help="")
    doc_query_parse.add_argument("--query", default="", help="")
    doc_query_parse.add_argument("--source_dir", default=".", help="")
    doc_query_parse.add_argument("--model", default="", help=desc["model"])
    doc_query_parse.add_argument("--emb_model", default="", help=desc["emb_model"])
    doc_query_parse.add_argument("--file", default="", help=desc["file"])
    doc_query_parse.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )
    doc_query_parse.add_argument("--execute", action="store_true", help=desc["execute"])
    doc_query_parse.add_argument(
        "--collections",
        default="default",
        help="Comma-separated list of collections to search",
    )
    doc_query_parse.add_argument(
        "--description", default="", help="Description to route the query"
    )

    doc_chat_parse = doc_subparsers.add_parser("chat", help="")
    doc_chat_parse.add_argument("--file", default="", help=desc["file"])
    doc_chat_parse.add_argument("--model", default="", help=desc["model"])
    doc_chat_parse.add_argument("--emb_model", default="", help=desc["emb_model"])
    doc_chat_parse.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )
    doc_chat_parse.add_argument("--source_dir", default=".", help="")
    doc_chat_parse.add_argument(
        "--collections",
        default="default",
        help="Comma-separated list of collections to search",
    )
    doc_chat_parse.add_argument(
        "--description", default="", help="Description to route the query"
    )

    doc_serve_parse = doc_subparsers.add_parser("serve", help="")
    doc_serve_parse.add_argument("--file", default="", help=desc["file"])
    doc_serve_parse.add_argument("--model", default="", help=desc["model"])
    doc_serve_parse.add_argument("--emb_model", default="", help=desc["emb_model"])
    doc_serve_parse.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )
    doc_serve_parse.add_argument("--source_dir", default=".", help="")
    doc_serve_parse.add_argument("--host", default="", help="")
    doc_serve_parse.add_argument("--port", type=int, default=8000, help="")
    doc_serve_parse.add_argument("--uvicorn_log_level", default="info", help="")
    doc_serve_parse.add_argument("--allow_credentials", action="store_true", help="")
    doc_serve_parse.add_argument("--allowed_origins", default=["*"], help="")
    doc_serve_parse.add_argument("--allowed_methods", default=["*"], help="")
    doc_serve_parse.add_argument("--allowed_headers", default=["*"], help="")
    doc_serve_parse.add_argument("--api_key", default="", help="")
    doc_serve_parse.add_argument("--served_model_name", default="", help="")
    doc_serve_parse.add_argument("--prompt_template", default="", help="")
    doc_serve_parse.add_argument("--ssl_keyfile", default="", help="")
    doc_serve_parse.add_argument("--ssl_certfile", default="", help="")
    doc_serve_parse.add_argument("--response_role", default="assistant", help="")
    doc_serve_parse.add_argument(
        "--collections", default="default", help="Collection name for indexing"
    )

    agent_parser = subparsers.add_parser("agent", help="Run an agent")
    agent_subparsers = agent_parser.add_subparsers(dest="agent_command")

    planner_parser = agent_subparsers.add_parser("planner", help="Run the planner agent")
    planner_parser.add_argument("--source_dir", default=".", help="Source directory")
    planner_parser.add_argument("--query", help="Query for the planner")    
    planner_parser.add_argument("--model", default="", help=desc["model"])
    planner_parser.add_argument("--emb_model", default="", help=desc["emb_model"])
    planner_parser.add_argument("--file", default="", help=desc["file"])
    planner_parser.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )
    planner_parser.add_argument("--execute", action="store_true", help=desc["execute"])
    planner_parser.add_argument(
        "--collections",
        default="default",
        help="Comma-separated list of collections to search",
    )
    planner_parser.add_argument(
        "--description", default="", help="Description to route the query"
    )
    planner_parser.add_argument(
        "--enable_rag_search",
        nargs="?",
        const=True,
        default=False,
        help=desc["enable_rag_search"],
    )
    planner_parser.add_argument(
        "--enable_rag_context",
        nargs="?",
        const=True,
        default=False,
        help=desc["enable_rag_context"],
    )

    planner_parser.add_argument("--rag_token", default="", help="")
    planner_parser.add_argument("--rag_url", default="", help="")
    planner_parser.add_argument("--target_file", default="./output.txt", help="")

    init_parser = subparsers.add_parser("init", help=desc["init_desc"])
    init_parser.add_argument("--source_dir", required=True, help=desc["init_dir"])

    screenshot_parser = subparsers.add_parser(
        "screenshot", help=desc["screenshot_desc"]
    )
    screenshot_parser.add_argument("--urls", required=True, help=desc["screenshot_url"])
    screenshot_parser.add_argument(
        "--output", required=True, help=desc["screenshot_output"]
    )
    screenshot_parser.add_argument("--source_dir", default=".", help="")

    next_parser = subparsers.add_parser(
        "next", help="Create a new action file based on the previous one"
    )
    next_parser.add_argument("name", help="Name for the new action file")
    next_parser.add_argument("--source_dir", default=".", help="")
    next_parser.add_argument("--from_yaml", help=desc["next_from_yaml"])

    doc2html_parser = subparsers.add_parser(
        "doc2html", help="Convert word/pdf document to html"
    )
    doc2html_parser.add_argument("--file", default="", help=desc["file"])
    doc2html_parser.add_argument("--model", default="", help=desc["model"])
    doc2html_parser.add_argument("--vl_model", default="", help=desc["vl_model"])
    doc2html_parser.add_argument(
        "--ray_address", default="auto", help=desc["ray_address"]
    )
    doc2html_parser.add_argument("--source_dir", default=".", help="")
    doc2html_parser.add_argument(
        "--urls", help="URL or path of the word/pdf document to convert"
    )
    doc2html_parser.add_argument(
        "--output", help="Output directory to save the converted html file"
    )

    if input_args: 
        args = parser.parse_args(input_args)
    else:
        args = parser.parse_args()

    return AutoCoderArgs(**vars(args)), args
