"""
Copyright 2024 Anouar El Harrak

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from enum import Enum

class ETHEMESTATE(Enum):
  DEFAULT = 0
  FORESTLIGHT = 1
  FORESTDARK = 2
  AZURELIGHT = 3
  AZUREDARK = 4
  SUNVALLEYLIGHT = 5
  SUNVALLEYDARK = 6
  ALT = 7
  CLAM = 8
  VISTA = 9
  XPNATIVE = 10
  WINNATIVE = 11
  CLASSIC = 12
  
  def next(self):
    index = self.value + 1
    index %= len(ETHEMESTATE)
    return ETHEMESTATE(index)
    
  def prev(self):
    index = self.value - 1
    index %= len(ETHEMESTATE)
    return ETHEMESTATE(index)
    
  