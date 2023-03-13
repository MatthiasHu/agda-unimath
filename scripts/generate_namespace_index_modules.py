#!/usr/bin/env python3
# Run this script:
# $ python3 scripts/generate_namespace_index_modules.py

import os
import pathlib
import sys
import utils


def generate_title(namespace):
    return "# " + namespace.capitalize().replace("-", " ") + "\n"


def generate_imports(root, namespace):
    namespace_path = os.path.join(root, namespace)
    def agda_file_filter(f): return utils.isAgdaFile(
        pathlib.Path(os.path.join(namespace_path, f)))
    namespace_files = filter(agda_file_filter, os.listdir(namespace_path))

    import_statements = (utils.get_import_statement(
        namespace, module_file, public=True) for module_file in namespace_files)
    return "\n".join(sorted(import_statements))


agda_block_template = \
    '''```agda
module {namespace} where

{imports}
```
'''


def generate_agda_block(root, namespace):
    return agda_block_template.format(namespace=namespace, imports=generate_imports(root, namespace))


if __name__ == "__main__":

    status = 0
    root = "src"

    for namespace in utils.get_subdirectories_recursive(root):
        namespace_filename = os.path.join(root, namespace) + ".lagda.md"
        with open(namespace_filename, "a+") as namespace_file:
            pass
        with open(namespace_filename, "r+") as namespace_file:
            contents = namespace_file.read()

        oldcontents = contents

        title_index = contents.find("# ")
        if title_index > 0:
            print(
                f"Warning! Namespace file {namespace_filename} has title after first line.")
        elif title_index == -1:  # Missing title. Generate it
            contents = generate_title(namespace) + contents

        agda_block_start = contents.rfind("```agda\n")

        if agda_block_start == -1:
            # Must add agda block
            # Add at the end of the file
            contents += "\n" + generate_agda_block(root, namespace)
        else:
            agda_block_end = contents.find(
                "\n```\n", agda_block_start + len("```agda\n"))
            generated_block = generate_agda_block(root, namespace)

            if agda_block_end == -1:
                # An agda block is opened but not closed.
                # This is an error, but we can fix it
                print(
                    f"WARNING! agda-block was opened but not closed in {namespace_filename}.")
                contents = contents[:agda_block_start] + generated_block
            else:
                agda_block_end += len("\n```\n")
                contents = contents[:agda_block_start] + \
                    generated_block + contents[agda_block_end:]

        if oldcontents != contents:
            status |= 1
            with open(namespace_filename, "w") as f:
                f.write(contents)

    sys.exit(status)