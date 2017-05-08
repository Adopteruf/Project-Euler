c = repmat(2:100, fliplr(size(2:100)));
disp(['The number of the distinct elements is ',num2str(length(unique((c(:)').^repmat(2:100, size(2:100))))),'.'])
