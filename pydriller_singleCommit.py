from pydriller import Repository
# repoPath = 'https://github.com/pimcore/pimcore'
repoPath = '../pimcore'
commitHash = '132fe2ea52489348185c7cef0e233983cf5ca85d'
for commit in Repository(repoPath, single=commitHash).traverse_commits(): #, single=commitHash
    print("modified files:", commit.files)
    print("modified lines:", commit.lines)
    print(commit.author.name)
    # for f in commit.modified_files:
    #     print("Filename:", f.filename)
    #     print("Number of Methods:", len(f.methods))
    #     print("Number of Lines of Code:", f.nloc)
    #     print("Complexity:", f.complexity)
    #     print("Token Count:", f.token_count)
    #     # print(f.source_code)
    #     # print(f.source_code_before)
