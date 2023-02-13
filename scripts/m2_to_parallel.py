import argparse
import os


def get_all_coder_ids(edits):
    coder_ids = set()
    for edit in edits:
        edit = edit.split("|||")
        coder_id = int(edit[-1])
        coder_ids.add(coder_id)
    coder_ids = sorted(list(coder_ids))
    return coder_ids


def m2_to_parallel(m2_files, ori, cor, drop_unchanged_samples, all):

    ori_fout = None
    if ori is not None:
        ori_fout = open(ori, 'w', encoding="utf-8")
    cor_fout = open(cor, 'w', encoding="utf-8")

    # Do not apply edits with these error types
    skip = {"noop", "UNK", "Um"}
    for m2_file in m2_files:
        import io
        entries = io.open(m2_file, encoding="utf-8").read().strip().split("\n\n")
        for entry in entries:
            lines = entry.split("\n")
            ori_sent = lines[0][2:]  # Ignore "S "
            cor_tokens = lines[0].split()[1:]  # Ignore "S "
            edits = lines[1:]
            offset = 0

            coders = get_all_coder_ids(edits) if all == True else [0]
            for coder in coders:
                offset = 0
                cor_tokens = lines[0].split()[1:]  # Ignore "S "
                for edit in edits:
                    edit = edit.split("|||")
                    if edit[1] in skip: continue  # Ignore certain edits
                    coder_id = int(edit[-1])
                    if coder_id != coder: continue  # Ignore other coders
                    span = edit[0].split()[1:]  # Ignore "A "
                    start = int(span[0])
                    end = int(span[1])
                    cor = edit[2].split()
                    cor_tokens[start + offset:end + offset] = cor
                    offset = offset - (end - start) + len(cor)

                cor_sent = " ".join(cor_tokens)
                if drop_unchanged_samples and ori_sent == cor_sent:
                    continue

                if ori is not None:
                    ori_fout.write(ori_sent + "\n")
                cor_fout.write(cor_sent + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', nargs='+', default=[])
    parser.add_argument('--erroneous_only', default=False, action='store_true', help='drop sentence without edits')
    parser.add_argument('--all_annotators', default=False, action='store_true', help='get all annotators')
    args = parser.parse_args()
    
    ori = []
    cor = []
    for filepath in args.data:
        path, ext = os.path.splitext(filepath)
        m2_to_parallel([filepath], path+'.src', path+'.tgt', args.erroneous_only, args.all_annotators)