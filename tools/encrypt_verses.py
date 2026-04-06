"""One-off helper to generate XOR+base64 verse payloads. Run: python tools/encrypt_verses.py"""
import base64
import json

KEY = b"WordPerfectV1ObfuscationKey"

VERSES = {
    "KJV": [
        {"ref": "Romans 3:10-11", "text": "As it is written, There is none righteous, no, not one: There is none that understandeth, there is none that seeketh after God."},
        {"ref": "Romans 3:23", "text": "For all have sinned, and come short of the glory of God;"},
        {"ref": "Romans 5:12", "text": "Wherefore, as by one man sin entered into the world, and death by sin; and so death passed upon all men, for that all have sinned:"},
        {"ref": "Romans 5:8", "text": "But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us."},
        {"ref": "Romans 6:23", "text": "For the wages of sin is death; but the gift of God is eternal life through Jesus Christ our Lord."},
        {"ref": "Romans 10:9-10", "text": "That if thou shalt confess with thy mouth the Lord Jesus, and shalt believe in thine heart that God hath raised him from the dead, thou shalt be saved. For with the heart man believeth unto righteousness; and with the mouth confession is made unto salvation."},
        {"ref": "Romans 10:13", "text": "For whosoever shall call upon the name of the Lord shall be saved."},
    ],
    "NIV": [
        {"ref": "Romans 3:10-11", "text": "As it is written: There is no one righteous, not even one; there is no one who understands; there is no one who seeks God."},
        {"ref": "Romans 3:23", "text": "for all have sinned and fall short of the glory of God,"},
        {"ref": "Romans 5:12", "text": "Therefore, just as sin entered the world through one man, and death through sin, and in this way death came to all people, because all sinned-"},
        {"ref": "Romans 5:8", "text": "But God demonstrates his own love for us in this: While we were still sinners, Christ died for us."},
        {"ref": "Romans 6:23", "text": "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord."},
        {"ref": "Romans 10:9-10", "text": "If you declare with your mouth, Jesus is Lord, and believe in your heart that God raised him from the dead, you will be saved. For it is with your heart that you believe and are justified, and it is with your mouth that you profess your faith and are saved."},
        {"ref": "Romans 10:13", "text": "for, Everyone who calls on the name of the Lord will be saved."},
    ],
    "ESV": [
        {"ref": "Romans 3:10-11", "text": "as it is written: None is righteous, no, not one; no one understands; no one seeks for God."},
        {"ref": "Romans 3:23", "text": "for all have sinned and fall short of the glory of God,"},
        {"ref": "Romans 5:12", "text": "Therefore, just as sin came into the world through one man, and death through sin, and so death spread to all men because all sinned-"},
        {"ref": "Romans 5:8", "text": "but God shows his love for us in that while we were still sinners, Christ died for us."},
        {"ref": "Romans 6:23", "text": "For the wages of sin is death, but the free gift of God is eternal life in Christ Jesus our Lord."},
        {"ref": "Romans 10:9-10", "text": "because, if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved. For with the heart one believes and is justified, and with the mouth one confesses and is saved."},
        {"ref": "Romans 10:13", "text": "For everyone who calls on the name of the Lord will be saved."},
    ],
    "NKJV": [
        {"ref": "Romans 3:10-11", "text": "As it is written: There is none righteous, no, not one; There is none who understands; There is none who seeks after God."},
        {"ref": "Romans 3:23", "text": "For all have sinned and fall short of the glory of God."},
        {"ref": "Romans 5:12", "text": "Therefore, just as through one man sin entered the world, and death through sin, and thus death spread to all men, because all sinned."},
        {"ref": "Romans 5:8", "text": "But God demonstrates His own love toward us, in that while we were still sinners, Christ died for us."},
        {"ref": "Romans 6:23", "text": "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord."},
        {"ref": "Romans 10:9-10", "text": "That if you confess with your mouth the Lord Jesus and believe in your heart that God has raised Him from the dead, you will be saved. For with the heart one believes unto righteousness, and with the mouth confession is made unto salvation."},
        {"ref": "Romans 10:13", "text": 'For "whoever calls on the name of the Lord shall be saved."'},
    ],
}


def enc(plain: str) -> str:
    data = plain.encode("utf-8")
    out = bytes(data[i] ^ KEY[i % len(KEY)] for i in range(len(data)))
    return base64.b64encode(out).decode("ascii")


def main():
    out = {}
    for ver, items in VERSES.items():
        out[ver] = [{"ref": x["ref"], "enc": enc(x["text"])} for x in items]
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
