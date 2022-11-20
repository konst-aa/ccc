(define (multiples-acc n multiple acc end)
  (let ((new (+ n multiple)))
       (if (< new end)
           (multiples-acc n new (+ acc new) end)
           acc)))

(print (- (+ (multiples-acc 5 0 0 1000)
             (multiples-acc 3 0 0 1000))
          (multiples-acc 15 0 0 1000)))
