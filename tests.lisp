
; simple test
(and A A B C)

; 
(not (if (if (or P (not Q)) R) (and P R)) (and P (not P) Q R (not P)))

; 
(or (not (if P Q)) (if R P) (if (and (not R) B) W))

; test for some complicated
(and A (not B) C (not D) (not (if (if (or C (not B)) A) (and D C))) (or (not (if B A)) (if C D) (if (and (not D) B) C)))

;
(and (if (and (not R) B) W) (or (not (if W B)) (if R W) (if (and (not R) B) W)))

; 
(and P (not P) A B (not A))

; 
(and (if P Q) (and P (not Q)) (not (if (iff (or P (not Q)) R) (and P R))))

; test for nested
(not (not (not (not (not P)))))

; test for another notation style
(and aa bb)


