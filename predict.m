function p = predict(theta, X)



m = size(X, 1); % Number of training examples

p = zeros(m, 1);



temp=X*theta;
temp=sigmoid(temp);

for i=1:m,
	if temp(i,1)>=0.5,
			p(i,1)=1;
	else
		p(i,1)=0;

end;


% =========================================================================


end
