# Add a new doc in collection 'cities' with ID 'LA'
db.collection("user").document("UserAuth2").set(data)
print("done")

doc_ref = db.collection(u'user').document(u'UserAuth')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')