
def punycode_encode(domain: str) -> str:
	"""
	Encode a Unicode domain name into Punycode (IDNA) format.
	"""
	return domain.encode("idna").decode("ascii")

def punycode_decode(domain: str) -> str:
	"""
	Decode a Punycode (IDNA) domain name back to its Unicode representation.
	"""
	return domain.encode("ascii").decode("idna")
