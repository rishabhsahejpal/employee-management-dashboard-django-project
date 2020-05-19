(function(){ //Immediately invoked function

	const animations = {
		// All show and hide functiions

		DOM : {
			project_to_remove : null,
			elem_updating_projects : null,
			ul : document.querySelector('div.project-section ul.projects')
		},

		VAR : {
			project_id : null,
			employee : null
		},

		hideObject : function(elem){
			elem.classList.add('hide')
			setTimeout(function(){
				elem.classList.add('d-none')
			},300);
		},

		showObject : function(elem){
			elem.classList.remove('hide');
			setTimeout(function(){
				elem.classList.remove('d-none');
			},300);
		},

		showForm : function(elem){
			const elems = this.getProjectElemsFromOptions(elem);
			this.showObject(elems.form);
			this.hideObject(elems.ul);
			this.hideObject(elems.h3);
		},

		hideForm : function(elem){
			const elems = this.getProjectElemsFromInsideForm(elem);
			this.hideObject(elems.form);
			this.showObject(elems.ul);
			this.showObject(elems.h3);
		},

		hideProjects : function(){document.querySelector('ul.projects').classList.add('hide');},
	
		showProjects : function(){document.querySelector('ul.projects').classList.remove('hide');},

		showProjectsLoading: function(){document.querySelector('div.projects-loading').classList.add('show');},
	
		hideProjectsLoading: function(){document.querySelector('div.projects-loading').classList.remove('show');},

		showModalBox : function(type){
			//Add overflow: hidden to body
			this.overflowHidden();
			//Load specific messgae
			document.querySelector('div.modal-content').innerHTML = this.showMessage(type);
			document.querySelector('div.modal-box').classList.remove('hidden');
		},
		
		hideModalBox : function(){
			//Remove overflow: hidden to body
			this.overflowRemove();
			document.querySelector('div.modal-box').classList.add('hidden');
			//Clear modal as well
			this.clearModal();
		},

		/* Inner Content altering functions */
		clearModal : function(){document.querySelector('div.modal-content').innerHTML = ''},

		loadMessageIntoProjectsLoading : function(type){document.querySelector('div.projects-loading').innerHTML = this.showMessage(type);},
	
		clearProjectsLoading : function(){document.querySelector('div.projects-loading').innerHTML = ''},

		showMessage : function(type){
			if (type == 'delete-permission')
				return '<span class="close close-modal"><span class="top"></span><span class="bottom"></span></span><h2>Do you want to proceed with deleting the project now?</h2><ul class="d-flex"><button class="delete-project-modal mr-3">Yes</button><button class="close-modal">No</button></ul>'	
		
			else if(type  == 'remove-user')
				return '<h2>Removing your project...</h2><div class="loader modal-load"><span class="circles"></span><span class="circles"></span><span class="circles"></span></div>'
		
			else if(type == 'update-project-list')
				return '<h2>Updating your projects\' list...</h2><div class="loader modal-load"><span class="circles"></span><span class="circles"></span><span class="circles"></span></div>'
		
			else if(type == 'update-project')
				return '<h2>Updating your project...</h2><div class="loader modal-load"><span class="circles"></span><span class="circles"></span><span class="circles"></span></div>'
		
			else if(type == 'adding-project')
				return '<h2>Adding your project...</h2><div class="loader modal-load"><span class="circles"></span><span class="circles"></span><span class="circles"></span></div>'
		
			else if(type == 'update-project-issue')
				return '<h2>Error: Cannot Update your project</h2>'
		
			else if(type == 'error-deleting')
				return '<h2>Error: Unable to remove your project. Please contact the support to fix this issue.</h2>'				
		
			else if(type == 'error-adding-project')
				return '<h2>Error: Unable to add your project. Please contact the support to fix this issue.</h2>'
		
			else if(type == 'error-updating')
				return '<h2>Error: Unable to update your project. Please contact the support to fix this issue.</h2>'
		
			else if(type == 'empty-projects')
				return '<h2>No projects to display</h2>'
		
			else if(type == 'empty-input')
				return '<h2>Please enter a valid project name...</h2>'
		
			else if(type == 'error-empty-input')
				return '<i class="fas fa-exclamation-triangle"></i><strong>Error : </strong>Please enter a valid project name'
		
			else if(type == 'error-no-assign')
				return '<i class="fas fa-exclamation-triangle"></i><strong>Error : </strong>Please assign the project'
		
			else if(type == 'error-nothing')
				return '<i class="fas fa-exclamation-triangle"></i><strong>Error : </strong>Please choose a project name and assign it'

			else if(type == 'add-project'){
				let dialog = '<span class="close close-modal"><span class="top"></span><span class="bottom"></span></span>'
				dialog += '<h2>Add a new project</h2><form action="#"><span class="error hide"></span><label for="name"><i class="fas fa-align-justify"></i>Choose a project name</label>'
				dialog += '<input type="text" name=\'name\' id=\'name\' placeholder=\'Choose a name for new project\'/>'
				dialog += '<h3><i class="fas fa-align-justify"></i>Assign memebers to the project</h3><div class="checkboxes"><div class="checkbox-wrap" data-id="1">'
				dialog += '<i class="fas fa-edit"></i><input type="checkbox" value=\'1\' name=\'1\'/><label for="1">John Markwell</label></div><div class="checkbox-wrap" data-id="2">'
				dialog += '<i class="fas fa-edit"></i><input type="checkbox" value=\'2\' name=\'2\'/><label for="2">Robert Doe</label></div><div class="checkbox-wrap" data-id="3">'
				dialog += '<i class="fas fa-edit"></i><input type="checkbox" value=\'3\' name=\'3\'/><label for="3">Jane Mitchell</label></div><div class="checkbox-wrap" data-id="4">'
				dialog += '<i class="fas fa-edit"></i><input type="checkbox" value=\'4\' name=\'4\'/><label for="4">Alicia Smith</label></div><div class="checkbox-wrap" data-id="5">'
				dialog += '<i class="fas fa-edit"></i><input type="checkbox" value=\'5\' name=\'5\'/><label for="5">Robert Maxwell</label></div><div class="checkbox-wrap" data-id="6">'
				dialog += '<i class="fas fa-edit"></i><input type="checkbox" value=\'6\' name=\'6\'/><label for="6">James Smith</label></div></div>'
				dialog += '<button type="button" class="add-project">Add <i class="fas fa-plus-square"></i></button></form>'

				return dialog
			}

			else 
				return true;
		},

		// End of show and hide functions

		// Fnctions to get elements

		findElemForPerformance : function(elem){
			return {
				heading : elem.closest('div.heading'),
				monthly : $(elem.closest('div.heading')).siblings('.monthly.op')[0],
			 	yearly : $(elem.closest('div.heading')).siblings('.yearly.op')[0]
			}
		},

		findElemForKPI : function(elem){
			return {
				heading : elem.closest('div.heading'),
				monthly : $(elem.closest('div.heading')).siblings('.kpi-container').children('ul.monthly.kpis')[0],
			 	yearly : $(elem.closest('div.heading')).siblings('.kpi-container').children('ul.yearly.kpis')[0]
			}
		},

		findElemForStats : function(elem){
			return {
				heading : elem.closest('div.heading'),
				monthly : $(elem.closest('div.heading')).siblings('ul.monthly.stats')[0],
			 	yearly : $(elem.closest('div.heading')).siblings('ul.yearly.stats')[0]
			}
		},

		getProjectElemsFromOptions : function(elem){
			return{
				form : $(elem.closest('li.d-flex')).children('form')[0],
				ul : elem.closest('ul.options'),
				h3 : $(elem.closest('ul.options')).siblings('h3')[0]
			}
		},

		getProjectElemsFromInsideForm : function(elem){
			return{
				form : $(elem.closest('li.d-flex')).children('form')[0],
				ul : $(elem.closest('form')).siblings('ul.options')[0],
				h3 : $(elem.closest('form')).siblings('h3')[0]
			}
		},

		// End of functions ot get elements

		// Navigation
		navigation : function(context){
			const open = document.querySelector('header div.col-menu')
			const close = document.querySelector('section.navigation span.close')
			open.addEventListener('click',function(){context.openNav(context)})
			close.addEventListener('click',function(){context.closeNav(context)})
		},

		openNav : function(context){
			const nav = document.querySelector('section.navigation')
			context.overflowHidden();
			nav.classList.remove('hidden');
		},

		closeNav : function(context){
			context.overflowRemove();
			const nav = document.querySelector('section.navigation')
			nav.classList.add('hidden');
		},

		overflowHidden : function(){document.querySelector('body').classList.add('overflow-hidden')},

		overflowRemove : function(){document.querySelector('body').classList.remove('overflow-hidden')},

		// Switching periods

		switchActive : function(elem){
			elem.classList.add('active')
			$(elem).parent('li').siblings().children('a')[0].classList.remove('active');
		},

		switchBetweenMonthlyAndYearly : function(elem,allElems){
			this.switchActive(elem);

			if(elem.classList.contains('monthly')){
				this.showObject(allElems.monthly);
				this.hideObject(allElems.yearly);
			}else if(elem.classList.contains('yearly')){
				this.showObject(allElems.yearly);
				this.hideObject(allElems.monthly);
			}
		},

		switchPeriod : function(elem,event){
			// All cases
			if(elem.classList.contains('op')){
				const allElems = this.findElemForPerformance(elem);
				this.switchBetweenMonthlyAndYearly(elem,allElems);

			}else if(elem.classList.contains('kpis')){
				const allElems = this.findElemForKPI(elem);
				this.switchBetweenMonthlyAndYearly(elem,allElems);

			}else if(elem.classList.contains('stats')){
				const allElems = this.findElemForStats(elem);
				this.switchBetweenMonthlyAndYearly(elem,allElems);

			}
		},
	
		switchPeriodClick : function(){
			const btns = document.querySelectorAll('.switch-period');
			btns.forEach( (elem,i)=>{
				elem.addEventListener('click', event=>{
					event.preventDefault();
					this.switchPeriod(elem,event);
				})
			});
		},

		editProjectClick : function(){
			this.DOM.ul.addEventListener('click',event=>{
				if(event.target.matches('.edit-project') || event.target.matches('.edit-project i')){
					event.preventDefault();
					this.showForm(event.target);
				}
			});
		},

		closeModalBox : function(context){
			const modal =  $(document.querySelector('div.modal-box'));
			modal.on('click','.close-modal',function(){
				context.hideModalBox();
			});
		},

		cancelEditProjectClick : function(){
			this.DOM.ul.addEventListener('click',event=>{
				if(event.target.matches('button.cancel') || event.target.matches('button.cancel i')){
					event.preventDefault();
					this.hideForm(event.target);
					//Empty input text
					this.emptyTextInput( $(event.target).siblings('input[type="text"]')[0] );
				}
			});
		},

		updateHeading : function(data){
			const elems = this.getProjectElemsFromInsideForm(this.DOM.elem_updating_projects);
			$(elems.h3).find('a').html('<i class="fas fa-project-diagram"></i> ' + data);
		},

		updatePlaceholder : function(data){
			const input = $(this.DOM.elem_updating_projects).siblings('input[type="text"]')[0];
			input.setAttribute('placeholder',data);
		},

		emptyTextInput : function(input){input.value = ''},

		saveEditProjectClick : function(context){
			this.DOM.ul.addEventListener('click',event=>{
				if(event.target.matches('button.save') || event.target.matches('button.save i')){
					//Set DOM element and project_id to be used later
					context.DOM.elem_updating_projects = (event.target.matches('button.save')) ? event.target : event.target.closest('button.save');
					context.VAR.project_id = event.target.getAttribute('data-id')

					let val = $(context.DOM.elem_updating_projects).siblings('input[type="text"]')[0].value 
					//If input is not empty
					if(val !== '' )
						context.update_db_ajax_call(val,context);
					else{
						// show modal with empty messgae
						context.showModalBox('empty-input');
						setTimeout(function(){
							context.hideModalBox();
						},2000)
					}
				}
			});
		},

		update_db_ajax_call : function(text,context){
			//Run check to see anything if you'd like			
			//Update the project heading
			//Hide Projects and show projects loading(with appropiate content)	
			context.showModalBox('update-project');		
			context.loadMessageIntoProjectsLoading();
			context.showProjectsLoading();
			context.hideProjects();

			$.ajax({
				url : ('/dashboard/ajax/update-project/'),
				type : 'POST',
				data : {'id' : context.VAR.project_id, 
						 'project_name' : text
				},	
				error: function(xhr, status, error) {
				  console.log(error);
				  console.log(xhr);
				  console.log(status);
				
				}
			}).done(function(data){
				if(data.text == 'project-name-updated'){
					// Remove the form and provide new heading 
					context.hideForm(context.DOM.elem_updating_projects);
					context.updateHeading(data.project_name);
					//Update place holder and empty text
					context.updatePlaceholder(data.project_name);
					context.emptyTextInput($(context.DOM.elem_updating_projects).siblings('input[type="text"]')[0]);
					//wait for 2sec before remving modal
					setTimeout(function(){
						context.hideModalBox();
						context.hideProjectsLoading();
						context.showProjects();
						context.clearProjectsLoading();
					},3000);
				}else{
					context.loadMessageIntoProjectsLoading('update-project-issue');
					setTimeout(function(){
						context.showModalBox('error-updating');
						setTimeout(function(){
							//Revert back to original
							context.hideModalBox();
							context.hideProjectsLoading();
							context.showProjects();
							context.clearProjectsLoading();

						},3000);
					},2000)		
				}
			});	
		},


		/*Remove project Functions*/
		showEmptyProjects : function(){
			this.loadMessageIntoProjectsLoading('empty-projects');
			this.showProjectsLoading();
		},

		checkProjectsLeft : function(){
			const len = document.querySelector('ul.projects').children.length;
			if(len == 0)
				this.showEmptyProjects();				
		},

		removeProjectListing : function(){
			this.DOM.project_to_remove.remove();
			//Check is no project is left
			this.checkProjectsLeft();
		},

		deleteProjectClick : function(){
			this.DOM.ul.addEventListener('click',event=>{
				if(event.target.matches('.delete-project') || event.target.matches('.delete-project i')){
					event.preventDefault();
					//Set the element to remove and set the id varaible
					this.DOM.project_to_remove = event.target.closest('li.d-flex');
					//Update variable so they can be used later on
					this.VAR.project_id = event.target.getAttribute('data-id');
					this.VAR.employee = event.target.getAttribute('data-employee');
	
					//Open Modal
					this.showModalBox('delete-permission')
				}
			});
		},

		deleteProjectFromModal : function(context){
			const modal = $(document.querySelector('div.modal-box'));
			modal.on('click','.delete-project-modal',function(){
				context.remove_user_db_ajax_call(context)
			});
		},

		remove_user_db_ajax_call : function(context){
			//Remove the user from project
			//Open model and load updating into it
			document.querySelector('div.modal-content').innerHTML = context.showMessage('remove-user');
			$.ajax({
				url : ('/dashboard/ajax/remove-user/'),
				type : 'POST',
				data : {'id' : this.VAR.project_id,
						'employee' : this.VAR.employee
				},
				error: function(xhr, status, error) {
					console.log(error);
					console.log(xhr);
					console.log(status);				
				}
			}).done(function(data){
				if(data == 'deleted-project-for-user'){
					//settimeouts for effect
					setTimeout(function(){
						document.querySelector('div.modal-content').innerHTML = context.showMessage('update-project-list');
						//Remove project from list
						context.removeProjectListing();
						setTimeout(function(){
							//Hide modal
							context.hideModalBox();
						},2000);
					},2000);	
				}else{
					setTimeout(function(){//Wait 2s before changing status
						document.querySelector('div.modal-content').innerHTML = context.showMessage('error-deleting');
						setTimeout(function(){
							context.hideModalBox();
						},2000);
					},2000);
				}
				
			});
		},
		/*End - Remove project functions*/

		showError : function(error,message,context){
			setTimeout(function(){
				error.innerHTML = context.showMessage(message)
				error.classList.remove('hide')},300);
				// error.innerHTML = '';
		},

		hideError : function(error){
			error.classList.add('hide')
			setTimeout(function(){
				error.innerHTML = ''
			},250)
		},

		chooseEmployee : function(context){
			const checkboxes = $(document.querySelector('div.modal-content')).find('div.checkbox-wrap'); 
			checkboxes.each(function(index,checkbox){
				if(checkbox.getAttribute('data-id') == context.VAR.employee){
					//Preselect the checkbox
					checkbox.classList.add('employee')
					$(checkbox).find('input[type=checkbox]')[0].setAttribute('checked','checked')
					return true;
				}
			})
		},
		
		addProjectClick : function(context){
			const click = document.querySelector('span.add-project')
			click.addEventListener('click',function(event){
				//Set employee id to be used later
				context.VAR.employee = click.getAttribute('data-id');
				context.showModalBox('add-project')
				context.chooseEmployee(context)
			});
		},

		addProjectFromModal : function(context){
			const modal = document.querySelector('div.modal-content');
			$(modal).on('click','button.add-project',function(){
				const error = $(modal).find('span.error')[0]
				//hide error everytime
				context.hideError(error)

				const input = $(this).siblings('input[type="text"]')[0]
				const checkboxes = $(this).siblings('div.checkboxes').find('input[type=checkbox]:checked')
				let checkBoxArray = [];
				if(input.value == '' && checkboxes.length == 0){
					context.showError(error,'error-nothing', context);
					return false
				}else if(input.value == ''){
					context.showError(error,'error-empty-input', context);
					return false
				}else if(checkboxes.length == 0){
					context.showError(error,'error-no-assign', context);
					return false
				}
				checkboxes.each(function(index,checkbox){
					checkBoxArray.push(checkbox.value);
				});

				let text = input.value;
				context.add_project_db_call(context,text,checkBoxArray);
			});
		},

		add_project_db_call : function(context,input,checkbox){
			//Remove the user from project
			//Open model and load updating into it
			document.querySelector('div.modal-content').innerHTML = context.showMessage('adding-project');
			$.ajax({
				url : ('/dashboard/ajax/add-project/'),
				type : 'POST',
				data : {'input' : input,
						'checkbox' : JSON.stringify(checkbox)
				},
				error: function(xhr, status, error) {
					console.log(error);
					console.log(xhr);
					console.log(status);				
				}
			}).done(function(data){
				if(data.text == 'added-project'){
					//settimeouts for effect
					setTimeout(function(){
						document.querySelector('div.modal-content').innerHTML = context.showMessage('update-project-list');
						//Remove project from list
						context.addProjectListing(context,input,data.id,data.assigned);
						setTimeout(function(){
							//Hide modal
							context.hideModalBox();
						},2000);
					},2000);	
				}else{
					setTimeout(function(){//Wait 2s before changing status
						document.querySelector('div.modal-content').innerHTML = context.showMessage('error-adding-project');
						setTimeout(function(){
							context.hideModalBox();
						},2000);
					},2000);
				}
			});
		},

		addProjectListing : function(context,text,id,assigned){
			let project = `<li class='d-flex'>
						<h3 class="justify-content-between flex-column align-items-start">
							<a href="#"><i class="fas fa-project-diagram"></i>${text}</a>
							<span><i class="fas fa-edit"></i>Assigned On: Today</span>
						</h3>
						<ul class="options">
							<li class="mr-3 edit-project" 
								data-employee='${context.VAR.employee}' 
								data-id="${id}"><i class="fas fa-pencil-alt"></i>Edit</li>
							<li class="delete-project" 
								data-employee='${context.VAR.employee}' 
								data-id="${id}"><i class="fas fa-trash"></i>Delete</li>
						</ul>
						<form action="#" method='POST' class='update-projects justify-content-center align-items-center d-none hide'>
							<i class="fas fa-project-diagram"></i>
							<input type="text" name="project" class="projects flex-grow-1" placeholder='${text}'/>
							<button data-id="${id}" type="button" class="save mr-2">
								<i class="fas fa-save"></i>
							</button>
							<button type="button" class="cancel">
								<i class="fas fa-times"></i>
							</button>
						</form>	
					</li>`
			$(document.querySelector('ul.projects')).prepend(project);
			// console.log(project)
		},

		removeLoader : function(){
			setTimeout(function(){
				document.querySelector('div.startup.loader').classList.remove('show');
				setTimeout(function(){
					document.querySelector('div.startup.loader').remove()
				},600);
			},2500);
		},

		loadBarsKPI : function(){
			const bars = document.querySelectorAll('div.kpi-meter .bar.load');
			const circles = document.querySelectorAll('div.kpi-meter .circle.load');
			const val = document.querySelectorAll('div.kpi-meter .value.load');
			let widths = []
			val.forEach(function(elem,i){
				widths.push(elem.getAttribute('data-width'))
			})

			setTimeout(function(){
				bars.forEach(function(bar,i){
					bar.style.width =  widths[i]+ '%'
				});
				circles.forEach(function(circle,i){
					circle.style.left = 'calc(' + widths[i] + '% - 6px)'
				});
				val.forEach(function(v,i){
					v.style.left="calc("+ widths[i] + "% - 0.6rem)"
					
				});
			},3500)

		},

		loadGraphOP : function(){
			const graph = document.querySelector('div.monthly div.graph-wrap.load path');
			const val = graph.getAttribute('data-stroke')
			setTimeout(function(){
				graph.setAttribute('stroke-dasharray',''+val+",100")
			},3500)

		},

		loadNumbersOP : function(){
			const value = document.querySelectorAll('div.kpi-meter .value.load');
			setTimeout(function(){
				
				value.forEach(function(v,i){
					let val = v.getAttribute('data-width')
					let parts = val/17;
					let valueInsert = 0;
					timer = setInterval(function(){
						valueInsert += parts;
						if(valueInsert <= val){
							v.innerHTML = Math.ceil(valueInsert) + '%'	
						}else if(valueInsert >= val && valueInsert <= val+5){
							v.innerHTML = val + '%'	
						}
						else
							clearInterval(timer);
					},25);
				});

			},3500)
		},

		loadNumbersKPI : function(){
			const num = document.querySelector('div.monthly div.graph-wrap.load p');
			const val = document.querySelector('div.monthly div.graph-wrap.load path').getAttribute('data-stroke')
			let parts = val/17;
			let valueInsert = 0;
			setTimeout(function(){
				timer = setInterval(function(){
					valueInsert += parts;
					if(valueInsert <= val){
						num.innerHTML = Math.ceil(valueInsert) + '%'	
					}else if(valueInsert >= val && valueInsert <= val+5){
						num.innerHTML = val + '%'	
					}
					else
						clearInterval(timer);
				},25);
			},3500)
		},

		clickPerformSwitch : function(context){
			const click = document.querySelectorAll('div.employee-performance-section h4.clickop');
			click.forEach(function(elem){
				elem.addEventListener('click',function(){
					context.switchGraphs(context,elem);
				})
			});
		},

		switchGraphs : function(context,elem){
			$(elem).addClass('active').siblings('h4').removeClass('active')
			if(elem.classList.contains('score')){
				//Change heading
				$(elem).siblings('h2').html('<i class="fas fa-star-half-alt"></i> Overall Score</h2>')
				$(elem.closest('.row')).find('.score.graph').removeClass('hide')
				$(elem.closest('.row')).find('.efficiency.graph').addClass('hide')
			}	
			else if(elem.classList.contains('efficiency')){
				$(elem).siblings('h2').html('<i class="fas fa-cog"></i> Efficiency</h2>')
				$(elem.closest('.row')).find('.efficiency.graph').removeClass('hide')
				$(elem.closest('.row')).find('.score.graph').addClass('hide')
			}
		},

		disableProjectHeadingLinks : function(){
			this.DOM.ul.addEventListener('click',function(e){
				if(e.target.matches('ul.projects li h3 a')){
					e.preventDefault();
				}
			})
		},

		disableFormOnEnter : function(){
			$('body').on('keydown','form',function(e){
				if(e.keyCode == 13)
					return false;
			})
		},

		main : function(){
			let self = this
			if(document.querySelector('body.index')){//index

				self.switchPeriodClick();
				self.loadBarsKPI();
				self.loadGraphOP();
				self.loadNumbersOP();
				self.loadNumbersKPI();
				self.clickPerformSwitch(self);
				self.disableProjectHeadingLinks();
				self.disableFormOnEnter();

				if(document.querySelector('span.add-project')){ //##only for special mode as it includes buttons
					self.editProjectClick();
					self.deleteProjectClick();
					self.closeModalBox(self);
					self.saveEditProjectClick(self);
					self.cancelEditProjectClick();
					self.deleteProjectFromModal(self);
					self.addProjectClick(self);
					self.addProjectFromModal(self);	
				}	
			}
				
			
			if(document.querySelector('section.navigation'))//Only for index, resources and docs
				this.navigation(this);

			this.removeLoader();//For all pages
		}
	}

	// Main
	animations.main();

})();