"Copyright 2022 Tsvi Benson-Tilsen
"Licensed under the GNU General Public License. See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

" Title:        Multisheets
" Description:  Multi-dimensional spreadsheets
" Maintainer:   Tsvi Benson-Tilsen; email provider is gmail, to tsvibtcontact

if exists("g:loaded_multisheets")
    finish
endif
let g:loaded_multisheets= 1

" Exposes the plugin's functions for use as commands in Vim.
command! -nargs=0 MSViewSheet call Multisheets#ViewSheet()
command! -nargs=0 MSViewSheetReinit call Multisheets#ViewSheetReinit()
command! -nargs=0 MSEnterFile call Multisheets#EnterFile()
command! -nargs=1 MSCycleArg call Multisheets#CycleArg(<f-args>)
command! -nargs=1 MSCycleProp call Multisheets#CycleProp(<f-args>)
command! -nargs=0 MSRenameProp call Multisheets#RenameProp()

 
