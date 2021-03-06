# Copyright 2017,2021 Niall McCarroll
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
from tests.test_utils import TestUtils
import unittest

class TestIterators(unittest.TestCase):
    

    def test_iterator_forwards(self):
        with TestUtils.open() as datastore:

            index = datastore.getIndex("X")
            
            l = list(map(lambda x:(x,200-x),list(range(1,201))))
    
            index.update(l)
            datastore.commit()

            self.assertEqual(len(index),200)
            for z in zip(index,l):
                (k1,v1) = z[0]
                (k2,v2) = z[1]
                self.assertEqual(k1,k2)
                self.assertEqual(v1,v2)

    def test_iterator_reverse(self):
        with TestUtils.open() as datastore:

            index = datastore.getIndex("X")
            
            l = list(map(lambda x:(x,200-x),list(range(200,0,-1))))

            index.update(l)
            datastore.commit()

            self.assertEqual(len(index),200)
            for z in zip(index.rtraverse(),l):
                (k1,v1) = z[0]
                (k2,v2) = z[1]
                self.assertEqual(k1,k2)
                self.assertEqual(v1,v2)


if __name__ == '__main__':
    unittest.main()