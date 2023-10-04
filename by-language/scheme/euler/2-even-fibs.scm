(define (allfibs a b acc)
  (let ((new (+ a b)))
       (if (< new 4000000)
           (allfibs b new (cons new acc))
           acc)))

(display (fold (lambda (item sum) (+ item sum))
               0
               (filter even? (allfibs 0 1 '(1 0)))))
