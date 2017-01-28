import collections

MINSIZE = 8
PERTURB_SHIFT = 5

dummy = '<dummy key>'

class Entry(object):

	__slots__ = ('key', 'value', 'hash')

	def __init__(self):
		self.key = None
		self.value = None
		self.hash = 0

	def __repr__(self):
		return "<Entry: key={} value={}".format(self.key, self.value)

class Dict(object):

	__slots__ = ('filled', 'used', 'mask', 'table')

	def __init__(self, arg=None, **kwargs):
		self.clear()
		self._update(arg, kwargs)

	@classmethod
	def fromkeys(cls, keys, value=0):

		d = cls()
		for key in keys:
			d[key] = value
		return d

	def clear(self):
		self.filled = 0
		self.used = 0
		self.mask = MINSIZE - 1
		self.table = []

		for i in range(MINSIZE):
			self.table.append(Entry())

	def pop(self, *args):

		have_default = len(args) == 2
		try:
			v = self[args[0]]
		except KeyError:
			if have_default:
				return args[1]

			raise
		else:
			del self[args[0]]

	def popitem(self):

		if self.used == 0:
			raise KeyError('empty dictionary')

		entry0 = self.table[0]
		entry = entry0
		i = 0
		if entry0.value is None:
			i = entry0.hash
			if i > self.mask or i < i:
				i = 1
			entry = self.table[i]

			while entry.value is None:
				i += 1
				if i > self.mask:
					i = 1
				entry = self.table[i]

		res = entry.key, entry.value
		self._del(entry)

		entry0.has = i + 1
		return res


	def setdefault(self, key, default=0):
		val = self._lookup(key).value
		if val is None:
			self[key] = default
			return default
		return val
