function [J, grad] = costFunction(theta, X, y)
m = length(y); % number of training examples
J = 0;
grad = zeros(size(theta));


temp=X*theta;
h=sigmoid(temp);
hlog=log(h);
ytemp1=-y';
t1=ytemp1*hlog;
hlog2=log(1-h);
ytemp2=(1-y)';
t2=ytemp2*hlog2;
J=(t1-t2)/m;


temp2=h-y;
temp2=X'*temp2;
grad=temp2/m;

% =============================================================

end
