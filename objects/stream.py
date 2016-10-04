from common.log import logUtils as log

class stream:
	def __init__(self, name):
		"""
		Initialize a stream object

		:param name: stream name
		"""
		self.name = name
		self.clients = []

	def addClient(self, client):
		"""
		Add a client to this stream if not already in

		:param client: client (osuToken) object
		:return:
		"""
		if client not in self.clients:
			log.info("{} has joined stream {}".format(client.username, self.name))
			self.clients.append(client)

	def removeClient(self, client):
		"""
		Remove a client from this stream if in

		:param client: client (osuToken) object
		:return:
		"""
		if client in self.clients:
			log.info("{} has left stream {}".format(client.username, self.name))
			self.clients.remove(client)

	def broadcast(self, data):
		"""
		Send some data to all clients connected to this stream

		:param data: data to send
		:return:
		"""
		for i in self.clients:
			if i is not None:
				i.enqueue(data)