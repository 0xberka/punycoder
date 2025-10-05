
# Punycoder
**Punycoder** is a Python tool to encode Unicode domain names into Punycode (IDNA) format and decode Punycode back into Unicode. It is useful for anyone working with **Internationalized Domain Names (IDNs)**.
> See: [RFC 3490](https://tools.ietf.org/html/rfc3490) - Internationalizing Domain Names in Applications (IDNA)

## Features
- Encode Unicode domain names to Punycode.
- Decode Punycode domain names back to Unicode.
- Command-line interface (CLI)
- Lightweight, dependency-free, Pythonic
- Compatible with Python 3.5+

## Usage

Encode a Unicode domain to Punycode:
```shell
./punycoder -e café.com
# Output: xn--caf-dma.com
```

Decode a Punycode domain to Unicode:
```shell
./punycoder -d xn--caf-dma.com
# Output: café.com
```

Invalid inputs are printed to stderr:
```shell
./punycoder -d xn--invalid--domain
# Error: decoding with 'idna' codec failed (UnicodeError: Violation of BIDI requirement 2)
```
