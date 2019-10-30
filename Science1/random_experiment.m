probdis = zeros(10000);
 for i N = 1:10000;
for j = 1:100
    x = zeros(N);
    x1 = zeros(N);
    a = 0;
    b = 1;
    r = (b-a).*rand(N,1) + a;
    r1 = (b-a).*rand(N,1) + a;
    for i=1:N
        if r(i)<0.5
        x(i+1) = x(i) + 1;
        end
        if r(i)>=0.5
            x(i+1) = x(i) - 1;
        end
        if r1(i)<0.5
        x1(i+1) = x1(i) + 1;
        end
        if r1(i)>=0.5
            x1(i+1) = x1(i) - 1;
        end
    end
    if x(N+1) == x1(N+1)
        run = run + 1;
    end
end
prob = run/1000;
probdis(i) = prob;
end
n=100 ;
probdis1 = zeros(100);
for i=1:n
   probdis1(i) = (factorial(2*i)*((0.5)^(1*i)))/((factorial(i))^2);
end

figure(1)
plot(probdis,"r"); hold on;
plot (probdis1,"b");
grid
