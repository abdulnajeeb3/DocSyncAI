def update_documentation(changed_functions, model, index):
    try:
        print(f"Number of changed functions: {len(changed_functions)}")
        for func in changed_functions:
            func_embedding = model.encode([func])
            result = index.query(func_embedding, top_k=1)
            most_similar_doc_id = result['matches'][0]['id']
            if most_similar_doc_id == 'readme':
                print(f"Function '{func}' requires updates in README.md")
            else:
                print("No changes were made that affect the readme.md")
    except Exception as e:
        print(f"Error updating documentation: {e}")
