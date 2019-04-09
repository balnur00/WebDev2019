import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { TaskList, Task } from '../shared/models/model';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  
  public tasksList: TaskList[] = [];
  public tasks: Task[] = [];
  
  ngOnInit() {
    this.provider.getTasksList().then(res => {
      this.tasksList = res;
      console.log(this.tasksList);
    })
  }

  getTaskFromList(tasklist: TaskList){
    this.provider.getTasks(tasklist.id).then(res=>{
      this.tasks = res;
      console.log(res);
    });
  }

}
