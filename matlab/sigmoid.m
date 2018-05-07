function g = sigmoid(z)
%SIGMOID Compute sigmoid function

g = zeros(size(z));

temp=e.^-(z);
    temp=temp.+1;
    temp=1./temp;
    g=temp;


end
