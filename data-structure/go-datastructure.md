## go-datastructure

1. stack 

   ```go
   type Stack struct {
       Values []int
   }
   
   func newStack() *Stack {
       return &Stack{st:make([]int, 0)} 
   }
   
   func (s *Stack) Push(x int) {
       s.Values = append(s.Values,x)
   }
   
   func (s *Stack) Peek() int {
       if len(s.Values) == 0{
           return nil
       }
       return s.Values[len(s.Values) - 1]
   }
   
   func (s *Stack) Pop() int {} {
       n := len(s.Values)
       if n == 0 {
           return nil
       }
       top := s.Values[n - 1]
       s.Values = s.Values[:n-1]
       return top
   }
   
   func (s *Stack) isEmpty() boolean {
       return len(s.Values) == 0
   }
   
   ```

   

2. queue

   ```go
   
   type Queue struct {
       Values []int
   }
   
   func NewQueue() *Queue {
       return &Queue{
           Values: make([]int, 0),
       }
   }
   func (q *Queue) Push(x int) {
       q.Values = append(q.Values, x)
   }
   
   func (q *Queue) Pop() int {
       if q.isEmpty() == true {
           return nil
       }
       x := q.Values[0]
       q.Values = q.Values[1:]
       return x
   }
   
   func (q *Queue) Front() Item {
       if 1.isEmpty() == true {
           return nil
       }
       return q.items[0]
   }
   
   func (q *Queue) End() Item {
       if q.isEmpty() == true {
           return nil
       }
       return q.Values[len(q.Values)-1]
   }
   
   func (q *Queue) isEmpty() bool {
       return len(q.Values) == 0
   }
   ```

   

3. 