%%  Ronaldo Sena
%   ronaldo.sena@outlook.com
%   December 2017
%   Use it as you please. If we meet some day, and you think
%   this stuff was helpful, you can buy me a beer
%
%   Ideal high pass filter. Takes a image and the mask radius and
%   oupts the filtered image
%
%   [outputImage] = idealHighPass(inputImage, radius, verbose)  

function [outputImage] = idealHighPass(inputImage, radius, verbose)    
    [rows, cols] = size (inputImage);
    if radius > min(rows,cols)
        radius = min(rows,cols);
    end
    radius = radius^2;    
    mask = zeros(rows,cols);
    centerX = rows/2;
    centerY = cols/2;
    for i = 1 : rows
        for j = 1 : cols
            dx = i - centerX;
            dx = dx^2;
            dy = j - centerY;
            dy = dy^2;
            mask(i, j) = dx + dy >= radius;
        end;
    end;    

    DFT  = fft2(inputImage);
    DFTC = fftshift(DFT);
    
    GC = mask .* DFTC;
    G = ifftshift(GC);
    outputImage = uint8(real(ifft2(G)));
    
    if ~exist('verbose','var')
        verbose = 'off';
    end
    if strcmp(verbose,'on')            
        if ~exist('plotResult','var')
            figure()
            imshow(mask)
            figure ();
            subplot (2,2,1);
            imshow (inputImage); 
            title 'Input Image'
            subplot (2,2,2);
            imshow (log(1+abs(DFTC)) , [3, 10]); 
            title 'Input Image FFT'
            subplot (2,2,3);
            imshow (outputImage); 
            title 'Output Image'
            subplot (2,2,4);
            imshow (log(1+abs(GC)) , [3, 10]); 
            title 'Output Image FFT'
        end
    end
end

