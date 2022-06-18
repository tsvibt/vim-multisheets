"Copyright 2022 Tsvi Benson-Tilsen
"Licensed under the GNU General Public License. See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

let g:multisheets_propdir = "propositions/"

let path = expand('<sfile>:p:h')
exec 'source' path . '/python-utilities.py'
exec 'source' path . '/python-multisheets.py'

" convenience autocommand if you're frequently resizing the terminal window with nvim, resizes the sheet to fit.
"autocmd VimResized * call Multisheets#MaybeViewSheet()
"set splitbelow

function! Multisheets#Py(fun,args)
	let g:ms_python_returnval=''
	python3 VimPython()
	return g:ms_python_returnval
endfunction

function! Multisheets#MaybeViewSheet()
	let ffile = Multisheets#Py('vim_Maybe_File_Fsheet' ,@%)
   exe "e " .ffile
endfunction

function! Multisheets#ViewSheet()
	let ffile = Multisheets#Py('vim_File_Fsheet' ,@%)
   exe "e " .ffile
endfunction

function! Multisheets#ViewSheetReinit()
	let ffile = Multisheets#Py('vim_File_Fsheet' ,@%)
	call delete(fnameescape(ffile))
	call Multisheets#ViewSheet()
endfunction

function! Multisheets#EnterFile()
	let ffiles = Multisheets#Py('vim_File_Word_Line_Files' ,[@%, expand("<cword>"), line('.'), virtcol('.')])
   for ffile in ffiles
      split
      exe "e " .ffile
   endfor
endfunction

function! Multisheets#CycleArg(n)
	let gotocol = Multisheets#Py('vim_CycleArg', [@%, a:n, virtcol('.'), line('.')])
	edit
   normal! 0
   if str2nr(gotocol) > 0
      exe "normal! " . gotocol . "l"
   endif
endfunction

function! Multisheets#CycleProp(n)
	let ffile = Multisheets#Py('vim_CycleProp', [@%, a:n])
   exe "e " .ffile
endfunction

function! Multisheets#RenameProp()
   let ffile = Multisheets#Py('vim_MaybeRenameFile', [@%, line('.')])
	if ffile == 'None'
      echo 'prop file with that name already exists or something went wrong'
   else
      exe "e " . ffile
   endif
endfunction
