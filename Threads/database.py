import pymongo # pip install pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def insert_sensor_data(self, sensor_data):
        try:
            self.collection.insert_one(sensor_data)
            print("Dados do sensor inseridos com sucesso!")
        except Exception as e:
            print(e)
