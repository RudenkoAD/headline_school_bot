from dataclasses import dataclass
@dataclass
class State:
  state_id:int
  text:str
  next_id_no:int
  next_id_yes:int
  next_id_silence:int
  