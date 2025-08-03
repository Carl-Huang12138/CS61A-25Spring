(define (over-or-under num1 num2) 
        (cond ((< num1 num2) -1)
              ((= num1 num2) 0)
              (else 1)))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
    (if (zero? (min a b)) (max a b)
        (gcd (min a b) (modulo (max a b) (min a b)))))

(define (remove item lst) (filter (lambda (x) (not (= x item))) lst))

(define (duplicate lst) 
    (if (null? lst)
        nil
        (cons (car lst)
              (cons (car lst)
                        (duplicate (cdr lst))))))

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (composed f g) 
    (lambda (x) (f(g x))))

(define (repeat f n) 
    (if (= n 1)
    f
    (composed f (repeat f (- n 1)))))

