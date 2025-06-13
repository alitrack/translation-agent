import glob

from app import convert


if __name__ == "__main__":
    path = "/Users/m2max/ws/jobs/duckdb in action/cn"
    path_zh = "/Users/m2max/ws/jobs/duckdb in action/cn/zh_r1"

    files = glob.glob(path + "/en/*/*.md", recursive=True)
    for f in files:
        #     if (
        #         "chapter_0_" in f
        #         or "chapter_1_" in f
        #         or "chapter_2_" in f
        #         or "chapter_3_" in f
        #     ):
        #         continue
        base_name = f.split("/")[-1]
        print(base_name)
        out_path = path_zh + "/ch_" + base_name.split("_")[1] + ".md"
        convert(f, out_path)
