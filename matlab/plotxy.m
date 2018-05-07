data = load('data.arff');
X=[data(:,1:17) data(:,19:19) data(:,21:26) data(:,28:28)];
y=data(:,end:end);

test= load('test.arff');
Xtest=[test(:,1:17) test(:,19:19) test(:,21:26) test(:,28:28)];
ytest=test(:,end:end);

[m, n] = size(X);
result=zeros(10,1);
i=1000;
xplot=zeros(10,1);
while (i<m),
	j=i/100;
	x1=X(1:i,:);
	y1=y(1:i,:);
	x1 = [ones(size(x1,1), 1) x1];
	initial_theta = zeros(n + 1, 1);
	options = optimset('GradObj', 'on', 'MaxIter', 1500);
[theta, cost] = ...
	fmincg(@(t)(costFunction(t, x1, y1)), initial_theta, options);
	result(j,1)=min(cost);
	xplot(j,1)=i;

	i=i+100;


endwhile

plot(xplot,result)
xlabel('training set size');
ylabel('Cost');
