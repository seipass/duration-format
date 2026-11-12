from __future__ import annotations
def run(seconds):
 s=int(seconds); h,s=divmod(s,3600); m,s=divmod(s,60)
 return f"{h:02d}:{m:02d}:{s:02d}"
